#!/bin/bash
set -e

# Change to the repository root
cd "$(git rev-parse --show-toplevel)"

# Check if there are any Python files to lint
if find ops optimizer tests/py -name "*.py" -type f 2>/dev/null | grep -q .; then
    echo "Running ruff check on Python code..."
    ruff check ops/ optimizer/ tests/py/
    echo "Running ruff format check..."
    ruff format --check ops/ optimizer/ tests/py/
    echo "Python linting passed!"
else
    echo "No Python files to lint yet."
fi

