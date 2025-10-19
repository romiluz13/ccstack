#!/usr/bin/env python3
"""
Context Analysis Script

Analyzes project context for token efficiency and relevance scoring.
Based on Anthropic Skills best practices.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List


def count_tokens(text: str) -> int:
    """
    Estimate token count (rough approximation: 1 token ≈ 4 characters)
    For accurate counting, use tiktoken library.
    """
    return len(text) // 4


def analyze_file(file_path: Path) -> Dict:
    """Analyze a single file for context metrics."""
    try:
        content = file_path.read_text()
        return {
            "path": str(file_path),
            "lines": content.count('\n'),
            "tokens": count_tokens(content),
            "size_kb": file_path.stat().st_size / 1024
        }
    except Exception as e:
        return {
            "path": str(file_path),
            "error": str(e)
        }


def analyze_directory(directory: Path, extensions: List[str] = None) -> Dict:
    """
    Analyze all files in a directory for context optimization.
    
    Args:
        directory: Path to analyze
        extensions: File extensions to include (e.g., ['.ts', '.tsx', '.js'])
    
    Returns:
        Analysis report with token counts and recommendations
    """
    if extensions is None:
        extensions = ['.ts', '.tsx', '.js', '.jsx', '.py', '.md']
    
    files_analyzed = []
    total_tokens = 0
    total_files = 0
    
    for ext in extensions:
        for file_path in directory.rglob(f'*{ext}'):
            if 'node_modules' in file_path.parts or '.git' in file_path.parts:
                continue
                
            analysis = analyze_file(file_path)
            if 'error' not in analysis:
                files_analyzed.append(analysis)
                total_tokens += analysis['tokens']
                total_files += 1
    
    # Sort by token count (largest first)
    files_analyzed.sort(key=lambda x: x.get('tokens', 0), reverse=True)
    
    return {
        "summary": {
            "total_files": total_files,
            "total_tokens": total_tokens,
            "avg_tokens_per_file": total_tokens // max(total_files, 1)
        },
        "files": files_analyzed[:50],  # Top 50 largest files
        "recommendations": generate_recommendations(total_tokens, files_analyzed)
    }


def generate_recommendations(total_tokens: int, files: List[Dict]) -> List[str]:
    """Generate optimization recommendations based on analysis."""
    recommendations = []
    
    if total_tokens > 100000:
        recommendations.append("⚠️ Context exceeds 100k tokens - consider splitting into focused presets")
    
    if total_tokens > 50000:
        recommendations.append("💡 Use focused context loading: `pnpm ctx ui` or `pnpm ctx backend`")
    
    # Find files that are unusually large
    large_files = [f for f in files if f.get('tokens', 0) > 5000]
    if large_files:
        recommendations.append(f"📋 {len(large_files)} files exceed 5k tokens - consider splitting or summarizing")
    
    if len(files) > 100:
        recommendations.append("📦 Large file count - progressive disclosure recommended")
    
    return recommendations


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: python analyze-context.py <directory>")
        sys.exit(1)
    
    directory = Path(sys.argv[1])
    
    if not directory.exists():
        print(f"Error: Directory {directory} does not exist")
        sys.exit(1)
    
    print(f"🔍 Analyzing context in: {directory}")
    print()
    
    analysis = analyze_directory(directory)
    
    # Print summary
    summary = analysis['summary']
    print("=" * 60)
    print("CONTEXT ANALYSIS SUMMARY")
    print("=" * 60)
    print(f"Total Files: {summary['total_files']}")
    print(f"Total Tokens: {summary['total_tokens']:,}")
    print(f"Avg Tokens/File: {summary['avg_tokens_per_file']:,}")
    print()
    
    # Print recommendations
    if analysis['recommendations']:
        print("RECOMMENDATIONS:")
        print("-" * 60)
        for rec in analysis['recommendations']:
            print(f"  {rec}")
        print()
    
    # Print top 10 largest files
    print("TOP 10 LARGEST FILES:")
    print("-" * 60)
    for i, file in enumerate(analysis['files'][:10], 1):
        print(f"  {i}. {file['path']}")
        print(f"     Tokens: {file['tokens']:,} | Lines: {file['lines']} | Size: {file['size_kb']:.1f}KB")
    print()
    
    # Save full report
    report_path = directory / "context-analysis-report.json"
    with open(report_path, 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print(f"📄 Full report saved to: {report_path}")


if __name__ == "__main__":
    main()

