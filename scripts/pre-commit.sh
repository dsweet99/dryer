#!/bin/bash
set -e

# Change to the repository root
cd "$(git rev-parse --show-toplevel)"

echo "=== Running Rust lints (clippy) ==="
./scripts/pre-commit-clippy.sh

echo ""
echo "=== Running Python lints (ruff) ==="
./scripts/pre-commit-ruff.sh

echo ""
echo "=== All pre-commit checks passed! ==="

