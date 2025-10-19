#!/bin/bash

# Pre-Commit Validation
# Runs basic validation before committing code

set -euo pipefail

echo ""
echo "🔍 Pre-Commit Validation"
echo ""

# Check for TODO/FIXME/HACK comments in staged files
STAGED_FILES=$(git diff --cached --name-only --diff-filter=ACM 2>/dev/null || echo "")

if [ -z "$STAGED_FILES" ]; then
    echo "ℹ️  No files staged for commit"
    exit 0
fi

# Count issues
TODO_COUNT=0
LARGE_FILE_COUNT=0
NO_TEST_COUNT=0

# Check each staged file
while IFS= read -r file; do
    if [ -f "$file" ]; then
        # Check for TODO/FIXME
        if grep -qE "TODO|FIXME|HACK|XXX" "$file" 2>/dev/null; then
            TODO_COUNT=$((TODO_COUNT + 1))
        fi
        
        # Check file size (> 500 lines warning)
        LINE_COUNT=$(wc -l < "$file" | tr -d ' ')
        if [ "$LINE_COUNT" -gt 500 ]; then
            LARGE_FILE_COUNT=$((LARGE_FILE_COUNT + 1))
        fi
        
        # Check if source file has tests
        if [[ "$file" =~ \.(ts|js|py|java|go)$ ]] && [[ ! "$file" =~ (test|spec|\__tests\__) ]]; then
            TEST_FILE=""
            case "$file" in
                *.ts|*.js)
                    TEST_FILE=$(echo "$file" | sed 's/\(\.ts\|\.js\)$/.test\1/')
                    ;;
                *.py)
                    TEST_FILE=$(echo "$file" | sed 's/\.py$/test_\1/')
                    ;;
            esac
            if [ -n "$TEST_FILE" ] && [ ! -f "$TEST_FILE" ]; then
                NO_TEST_COUNT=$((NO_TEST_COUNT + 1))
            fi
        fi
    fi
done <<< "$STAGED_FILES"

# Report findings
if [ $TODO_COUNT -gt 0 ]; then
    echo "⚠️  $TODO_COUNT file(s) contain TODO/FIXME comments"
fi

if [ $LARGE_FILE_COUNT -gt 0 ]; then
    echo "⚠️  $LARGE_FILE_COUNT file(s) exceed 500 lines (consider splitting)"
fi

if [ $NO_TEST_COUNT -gt 0 ]; then
    echo "⚠️  $NO_TEST_COUNT source file(s) may lack tests"
fi

if [ $TODO_COUNT -eq 0 ] && [ $LARGE_FILE_COUNT -eq 0 ] && [ $NO_TEST_COUNT -eq 0 ]; then
    echo "✅ All validation checks passed"
fi

echo ""
echo "💡 Tip: Run /dotai:review before committing"
echo ""

# Always allow commit (warnings only)
exit 0

