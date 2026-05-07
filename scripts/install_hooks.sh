#!/bin/bash
# install_hooks.sh — Install git hooks for Projet_Automate
# Run once: bash scripts/install_hooks.sh

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HOOKS_DIR="$REPO_ROOT/.git/hooks"
PYTHON="/c/Users/silli/AppData/Local/Programs/Python/Python313/python.exe"

echo "Installing git hooks in $HOOKS_DIR..."

cat > "$HOOKS_DIR/post-commit" << EOF
#!/bin/bash
# post-commit hook — recalculate citedBy[] after every commit
# Note: .private/ is gitignored — citedBy changes are local only (not committed)
PYTHON="$PYTHON"
SCRIPT="\$(git rev-parse --show-toplevel)/scripts/backlinks_updater.py"
if [ -f "\$SCRIPT" ]; then
    "\$PYTHON" "\$SCRIPT" 2>&1
fi
EOF

chmod +x "$HOOKS_DIR/post-commit"
echo "Done. post-commit hook installed."
