#!/bin/bash

# Post-Edit Security Scanner
# Automatically scans edited files for common security issues

set -euo pipefail

FILE_PATH="${1:-}"

if [ -z "$FILE_PATH" ]; then
    exit 0
fi

if [ ! -f "$FILE_PATH" ]; then
    exit 0
fi

# Silent mode - only output if issues found
ISSUES_FOUND=false

# Check for hardcoded secrets
if grep -qE "(password|secret|api_key|token|auth).*(=|:)\s*['\"][^'\"]{8,}['\"]" "$FILE_PATH" 2>/dev/null; then
    if [ "$ISSUES_FOUND" = false ]; then
        echo ""
        echo "⚠️  Security Scan: $FILE_PATH"
        ISSUES_FOUND=true
    fi
    echo "   • Potential hardcoded secret detected"
fi

# Check for SQL injection risks
if grep -qE "(execute|query|sql).*\+|\".*\+.*SELECT|'.*\+.*SELECT" "$FILE_PATH" 2>/dev/null; then
    if [ "$ISSUES_FOUND" = false ]; then
        echo ""
        echo "⚠️  Security Scan: $FILE_PATH"
        ISSUES_FOUND=true
    fi
    echo "   • Potential SQL injection risk (string concatenation in query)"
fi

# Check for eval usage
if grep -qE "\beval\s*\(|exec\s*\(" "$FILE_PATH" 2>/dev/null; then
    if [ "$ISSUES_FOUND" = false ]; then
        echo ""
        echo "⚠️  Security Scan: $FILE_PATH"
        ISSUES_FOUND=true
    fi
    echo "   • Dangerous: eval() or exec() detected"
fi

# Check for insecure HTTP
if grep -qE "http://.*api|fetch\(['\"]http://" "$FILE_PATH" 2>/dev/null; then
    if [ "$ISSUES_FOUND" = false ]; then
        echo ""
        echo "⚠️  Security Scan: $FILE_PATH"
        ISSUES_FOUND=true
    fi
    echo "   • Insecure HTTP detected (should use HTTPS)"
fi

# Check for weak crypto
if grep -qE "MD5|SHA1(?!-)|\bDES\b" "$FILE_PATH" 2>/dev/null; then
    if [ "$ISSUES_FOUND" = false ]; then
        echo ""
        echo "⚠️  Security Scan: $FILE_PATH"
        ISSUES_FOUND=true
    fi
    echo "   • Weak cryptography algorithm detected (MD5/SHA1/DES)"
fi

if [ "$ISSUES_FOUND" = true ]; then
    echo ""
    echo "💡 Tip: Review security-hardening Skills for best practices"
    echo ""
fi

# Always exit 0 to not block the edit
exit 0

