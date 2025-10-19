#!/usr/bin/env python3
"""
OWASP Top 10 Security Checker

Automated checks for common security vulnerabilities based on OWASP Top 10.
Run this before committing code or during security reviews.
"""

import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple


class SecurityIssue:
    def __init__(self, severity: str, category: str, file: str, line: int, description: str, recommendation: str):
        self.severity = severity
        self.category = category
        self.file = file
        self.line = line
        self.description = description
        self.recommendation = recommendation


class OWASPChecker:
    def __init__(self):
        self.issues: List[SecurityIssue] = []
        
    def check_sql_injection(self, content: str, file_path: Path) -> None:
        """Check for potential SQL injection vulnerabilities."""
        # Pattern: String concatenation in SQL queries
        patterns = [
            (r'execute\s*\(\s*["\'].*?\+', 'SQL query with string concatenation'),
            (r'query\s*\(\s*["\'].*?\+', 'SQL query with string concatenation'),
            (r'SELECT.*?\+.*?FROM', 'Direct string concatenation in SELECT'),
            (r'WHERE.*?\$\{', 'Template literal in WHERE clause'),
        ]
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern, desc in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues.append(SecurityIssue(
                        severity='HIGH',
                        category='A03:2021 – Injection',
                        file=str(file_path),
                        line=i,
                        description=f'Potential SQL injection: {desc}',
                        recommendation='Use parameterized queries or ORM methods instead of string concatenation'
                    ))
    
    def check_xss_vulnerabilities(self, content: str, file_path: Path) -> None:
        """Check for Cross-Site Scripting (XSS) vulnerabilities."""
        patterns = [
            (r'innerHTML\s*=(?!.*sanitize)', 'innerHTML without sanitization'),
            (r'dangerouslySetInnerHTML', 'Using dangerouslySetInnerHTML'),
            (r'document\.write\s*\(', 'document.write() usage'),
            (r'eval\s*\(', 'eval() usage (code injection risk)'),
        ]
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern, desc in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues.append(SecurityIssue(
                        severity='HIGH',
                        category='A03:2021 – Injection',
                        file=str(file_path),
                        line=i,
                        description=f'Potential XSS vulnerability: {desc}',
                        recommendation='Sanitize user input, use textContent instead of innerHTML, avoid eval()'
                    ))
    
    def check_hardcoded_secrets(self, content: str, file_path: Path) -> None:
        """Check for hardcoded secrets and credentials."""
        patterns = [
            (r'password\s*=\s*["\'][^"\']+["\']', 'Hardcoded password'),
            (r'api[_-]?key\s*=\s*["\'][^"\']+["\']', 'Hardcoded API key'),
            (r'secret\s*=\s*["\'][^"\']+["\']', 'Hardcoded secret'),
            (r'token\s*=\s*["\'][a-zA-Z0-9]{20,}["\']', 'Hardcoded token'),
            (r'AWS_SECRET_ACCESS_KEY.*["\'][^"\']+["\']', 'AWS secret key'),
        ]
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            # Skip comments and test files
            if line.strip().startswith('//') or line.strip().startswith('#'):
                continue
            if 'test' in file_path.name.lower() or 'mock' in file_path.name.lower():
                continue
                
            for pattern, desc in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues.append(SecurityIssue(
                        severity='CRITICAL',
                        category='A07:2021 – Identification and Authentication Failures',
                        file=str(file_path),
                        line=i,
                        description=f'Potential hardcoded secret: {desc}',
                        recommendation='Use environment variables or secret management service (AWS Secrets Manager, Vault)'
                    ))
    
    def check_insecure_crypto(self, content: str, file_path: Path) -> None:
        """Check for insecure cryptographic practices."""
        patterns = [
            (r'md5\s*\(', 'MD5 usage (cryptographically broken)'),
            (r'sha1\s*\(', 'SHA-1 usage (weak)'),
            (r'Math\.random\s*\(\)', 'Math.random() for security (not cryptographically secure)'),
            (r'algorithm:\s*["\']HS256["\']', 'HS256 JWT algorithm (prefer RS256)'),
        ]
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern, desc in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues.append(SecurityIssue(
                        severity='MEDIUM',
                        category='A02:2021 – Cryptographic Failures',
                        file=str(file_path),
                        line=i,
                        description=f'Insecure cryptographic practice: {desc}',
                        recommendation='Use bcrypt for passwords, crypto.randomBytes() for tokens, RS256 for JWT'
                    ))
    
    def check_authentication_issues(self, content: str, file_path: Path) -> None:
        """Check for authentication and session management issues."""
        patterns = [
            (r'localStorage\.setItem.*token', 'Storing token in localStorage (XSS risk)'),
            (r'sessionStorage\.setItem.*token', 'Storing token in sessionStorage (XSS risk)'),
            (r'cookie.*secure:\s*false', 'Cookie without secure flag'),
            (r'cookie.*httpOnly:\s*false', 'Cookie without httpOnly flag'),
        ]
        
        lines = content.split('\n')
        for i, line in enumerate(lines, 1):
            for pattern, desc in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues.append(SecurityIssue(
                        severity='HIGH',
                        category='A07:2021 – Identification and Authentication Failures',
                        file=str(file_path),
                        line=i,
                        description=f'Authentication issue: {desc}',
                        recommendation='Use httpOnly, secure cookies or Authorization headers with short-lived tokens'
                    ))
    
    def check_file(self, file_path: Path) -> None:
        """Run all security checks on a file."""
        try:
            content = file_path.read_text()
            
            self.check_sql_injection(content, file_path)
            self.check_xss_vulnerabilities(content, file_path)
            self.check_hardcoded_secrets(content, file_path)
            self.check_insecure_crypto(content, file_path)
            self.check_authentication_issues(content, file_path)
            
        except Exception as e:
            print(f"Error checking {file_path}: {e}", file=sys.stderr)
    
    def scan_directory(self, directory: Path, extensions: List[str] = None) -> None:
        """Scan all files in directory."""
        if extensions is None:
            extensions = ['.js', '.ts', '.tsx', '.jsx', '.py', '.java', '.go']
        
        for ext in extensions:
            for file_path in directory.rglob(f'*{ext}'):
                if 'node_modules' in file_path.parts or '.git' in file_path.parts:
                    continue
                if 'test' in file_path.name.lower():
                    continue
                    
                self.check_file(file_path)
    
    def generate_report(self) -> str:
        """Generate security audit report."""
        if not self.issues:
            return "✅ No security issues found!"
        
        # Group by severity
        critical = [i for i in self.issues if i.severity == 'CRITICAL']
        high = [i for i in self.issues if i.severity == 'HIGH']
        medium = [i for i in self.issues if i.severity == 'MEDIUM']
        
        report = []
        report.append("=" * 80)
        report.append("OWASP SECURITY AUDIT REPORT")
        report.append("=" * 80)
        report.append(f"Total Issues: {len(self.issues)}")
        report.append(f"  🔴 Critical: {len(critical)}")
        report.append(f"  🟠 High: {len(high)}")
        report.append(f"  🟡 Medium: {len(medium)}")
        report.append("")
        
        for severity_name, issues in [('CRITICAL', critical), ('HIGH', high), ('MEDIUM', medium)]:
            if not issues:
                continue
                
            report.append(f"\n{severity_name} SEVERITY ISSUES:")
            report.append("-" * 80)
            
            for issue in issues:
                report.append(f"\n📍 {issue.file}:{issue.line}")
                report.append(f"   Category: {issue.category}")
                report.append(f"   Issue: {issue.description}")
                report.append(f"   Fix: {issue.recommendation}")
        
        return "\n".join(report)


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python owasp-checker.py <directory>")
        print("\nScans for OWASP Top 10 security vulnerabilities:")
        print("  - SQL Injection")
        print("  - XSS (Cross-Site Scripting)")
        print("  - Hardcoded secrets")
        print("  - Insecure cryptography")
        print("  - Authentication issues")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"Error: Directory {directory} does not exist")
        sys.exit(1)
    
    print(f"🔍 Scanning {directory} for security vulnerabilities...")
    print()
    
    checker = OWASPChecker()
    checker.scan_directory(directory)
    
    report = checker.generate_report()
    print(report)
    
    # Exit with error code if critical or high issues found
    critical_high = [i for i in checker.issues if i.severity in ['CRITICAL', 'HIGH']]
    if critical_high:
        print("\n⚠️  Build should FAIL - critical/high severity issues found!")
        sys.exit(1)
    else:
        print("\n✅ No critical or high severity issues found")
        sys.exit(0)


if __name__ == "__main__":
    main()

