#!/bin/bash
# Maverick Harness — Install Script (V0)
# Installs the harness into ~/.claude

set -e

HARNESS_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$HOME/.claude/maverick-harness"

echo "Maverick Harness — Installer V0"
echo "Source:  $HARNESS_DIR"
echo "Target:  $TARGET_DIR"
echo ""

# Create target directory
mkdir -p "$TARGET_DIR"

# Copy core files
cp -r "$HARNESS_DIR/verifier" "$TARGET_DIR/"
cp -r "$HARNESS_DIR/trap-project" "$TARGET_DIR/"
cp -r "$HARNESS_DIR/skills" "$TARGET_DIR/"
cp -r "$HARNESS_DIR/hooks" "$TARGET_DIR/"

# Make scripts executable
chmod +x "$TARGET_DIR/verifier/verify.py"
chmod +x "$TARGET_DIR/trap-project/run_traps.py"
chmod +x "$TARGET_DIR/hooks/end_of_session.py"

echo "Installed to $TARGET_DIR"
echo ""
echo "Verify installation:"
echo "  python3 $TARGET_DIR/trap-project/run_traps.py"
echo ""
echo "Expected output: ALL TRAPS BEHAVE"
