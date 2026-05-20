"""
Streamlit dashboard for Freelance Arbitrage Agent.
Run: streamlit run dashboard/app.py
"""

import sqlite3
import sys
from pathlib import Path

import pandas as pd
import streamlit as st
from openai import OpenAI

sys.path.insert(0, str(Path(__file__).parent.parent))
from db import get_db

DB_PATH = Path(__file__).parent.parent / "data" / "missions.db"

TOOL_LABELS = {
    "book_translator": "📚 Book Translator",
    "prooflab": "🔍 ProofLab",
    "whisper": "🎙 Whisper",
    "gpt_script": "🤖 GPT Script",
    "data_python": "📊 Python Data",
    "new_build": "🔨 Nouveau build",
    "none": "❌ Aucun",
}

SCORE_BADGE = lambda s: "🟢" if s >= 75 else ("🟡" if s >= 50 else "🔴")


def main():
    st.set_page_config(page_title="Freelance Arbitrage", page_icon="🎯", layout="wide")
    st.title("🎯 Freelance Arbitrage Agent")

    tab_opps, tab_discovery, tab_stats = st.tabs(["Opportunités", "Discovery", "Stats"])

    with tab_opps:
        render_opportunities()

    with tab_discovery:
        render_discovery()

    with tab_stats:
        render_stats()


def render_opportunities():
    st.subheader("Missions scorées")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        platform = st.selectbox("Plateforme", ["Toutes", "upwork", "fiverr"])
    with col2:
        tool = st.selectbox("Outil", ["Tous"] + list(TOOL_LABELS.keys()))
    with col3:
        min_score = st.slider("Score min", 0, 100, 50)
    with col4:
        min_budget = st.number_input("Budget min ($)", 0, 500, 15)

    df = load_missions(platform, tool, min_score, min_budget, exclude_new_build=True)

    if df.empty:
        st.info("Aucune mission trouvée. Lance un scan d'abord.")
        return

    for _, row in df.iterrows():
        render_mission_row(row)


def render_mission_row(row):
    score = int(row.get("total_score", 0))
    badge = SCORE_BADGE(score)
    tool_label = TOOL_LABELS.get(row.get("tool_match", "none"), "?")
    budget = _format_budget(row.get("budget_min"), row.get("budget_max"))
    delivery = f"{int(row['estimated_delivery_minutes'])} min" if row.get("estimated_delivery_minutes") else "?"

    with st.expander(f"{badge} [{score}/100] {row['title'][:80]} — {budget} | {tool_label}"):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(row.get("description", "")[:500])
            if row.get("url"):
                st.markdown(f"[Voir la mission →]({row['url']})")
            if row.get("scoring_reasoning"):
                st.caption(f"💬 {row['scoring_reasoning']}")
        with col2:
            st.metric("Score", f"{score}/100")
            st.metric("Livraison estimée", delivery)
            st.metric("Proposals", row.get("nb_proposals", "?"))

            if st.button("📝 Générer proposal", key=f"prop_{row['id']}"):
                proposal = generate_proposal(row)
                st.code(proposal, language="")

            result_options = ["", "hired", "rejected", "no_response"]
            current_result = row.get("result") or ""
            new_result = st.selectbox("Résultat", result_options, index=result_options.index(current_result) if current_result in result_options else 0, key=f"res_{row['id']}")
            if new_result and new_result != current_result:
                update_result(row["id"], new_result)
                st.success(f"Mis à jour : {new_result}")

            if not row.get("proposal_sent") and st.button("✅ Marquer soumis", key=f"sent_{row['id']}"):
                mark_proposal_sent(row["id"])
                st.success("Marqué comme soumis")


def render_discovery():
    st.subheader("🔨 Missions candidats nouveau build")
    st.caption("Missions où tool_match = new_build et build_score ≥ 1 — candidats backlog projets")

    df = load_missions_discovery()
    if df.empty:
        st.info("Aucune mission 'nouveau build' trouvée.")
        return

    for _, row in df.iterrows():
        score = int(row.get("total_score", 0))
        budget = _format_budget(row.get("budget_min"), row.get("budget_max"))
        with st.expander(f"[{score}/100] {row['title'][:80]} — {budget}"):
            st.write(row.get("description", "")[:500])
            if row.get("scoring_reasoning"):
                st.caption(f"💬 {row['scoring_reasoning']}")
            if row.get("url"):
                st.markdown(f"[Voir →]({row['url']})")


def render_stats():
    st.subheader("📊 Stats globales")

    with get_db(DB_PATH) as conn:
        total = pd.read_sql("SELECT COUNT(*) as n FROM missions", conn).iloc[0]["n"]
        alerted = pd.read_sql("SELECT COUNT(*) as n FROM missions WHERE alerted = 1", conn).iloc[0]["n"]
        sent = pd.read_sql("SELECT COUNT(*) as n FROM missions WHERE proposal_sent = 1", conn).iloc[0]["n"]
        hired = pd.read_sql("SELECT COUNT(*) as n FROM missions WHERE result = 'hired'", conn).iloc[0]["n"]

        tool_breakdown = pd.read_sql(
            "SELECT tool_match, COUNT(*) as n FROM missions WHERE tool_match IS NOT NULL GROUP BY tool_match ORDER BY n DESC",
            conn
        )

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Missions scrapées", int(total))
    col2.metric("Alertes envoyées", int(alerted))
    col3.metric("Proposals soumis", int(sent))
    col4.metric("Recrutements", int(hired))

    if not tool_breakdown.empty:
        st.subheader("Répartition par outil")
        tool_breakdown["tool_match"] = tool_breakdown["tool_match"].map(lambda x: TOOL_LABELS.get(x, x))
        st.bar_chart(tool_breakdown.set_index("tool_match")["n"])


def load_missions(platform, tool, min_score, min_budget, exclude_new_build=False) -> pd.DataFrame:
    conditions = [f"total_score >= {min_score}"]
    if platform != "Toutes":
        conditions.append(f"platform = '{platform}'")
    if tool != "Tous":
        conditions.append(f"tool_match = '{tool}'")
    if min_budget > 0:
        conditions.append(f"(budget_max >= {min_budget} OR budget_min >= {min_budget})")
    if exclude_new_build:
        conditions.append("tool_match != 'new_build'")

    where = " AND ".join(conditions)
    query = f"SELECT * FROM missions WHERE {where} ORDER BY total_score DESC LIMIT 100"

    with get_db(DB_PATH) as conn:
        return pd.read_sql(query, conn)


def load_missions_discovery() -> pd.DataFrame:
    query = "SELECT * FROM missions WHERE tool_match = 'new_build' AND build_score >= 1 ORDER BY total_score DESC LIMIT 50"
    with get_db(DB_PATH) as conn:
        return pd.read_sql(query, conn)


def generate_proposal(row) -> str:
    import os
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    tool_label = TOOL_LABELS.get(row.get("tool_match", "none"), "AI tools")
    delivery = f"{int(row['estimated_delivery_minutes'])} minutes" if row.get("estimated_delivery_minutes") else "quickly"

    prompt = f"""Generate a short, direct Upwork/Fiverr proposal for this mission.

Mission title: {row['title']}
Description: {row.get('description', '')[:400]}
Tool to use: {tool_label}
Estimated delivery: {delivery}

Rules:
- Under 80 words
- Lead with the delivery time and concrete outcome
- No buzzwords, no generic "I am a professional..."
- End with one specific question to engage the client
- Tone: direct, confident, no fluff"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
    )
    return response.choices[0].message.content.strip()


def mark_proposal_sent(mission_id: str):
    with get_db(DB_PATH) as conn:
        conn.execute("UPDATE missions SET proposal_sent = 1 WHERE id = ?", (mission_id,))
        conn.commit()


def update_result(mission_id: str, result: str):
    with get_db(DB_PATH) as conn:
        conn.execute("UPDATE missions SET result = ? WHERE id = ?", (result, mission_id))
        conn.commit()


def _format_budget(budget_min, budget_max) -> str:
    if budget_min is None and budget_max is None:
        return "Budget ?"
    if budget_min == budget_max or budget_min is None:
        return f"${int(budget_max or budget_min)}"
    return f"${int(budget_min)}-${int(budget_max)}"


if __name__ == "__main__":
    main()
