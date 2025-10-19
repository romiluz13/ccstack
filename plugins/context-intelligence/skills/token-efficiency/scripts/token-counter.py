#!/usr/bin/env python3
"""
Token Counter Script

Accurate token counting using tiktoken library (OpenAI's tokenizer).
Compatible with Claude's token counting (similar to GPT-4).
"""

import sys
from pathlib import Path

try:
    import tiktoken
except ImportError:
    print("⚠️  tiktoken not installed. Install with: pip install tiktoken")
    print("Falling back to approximation (1 token ≈ 4 characters)")
    tiktoken = None


def count_tokens_accurate(text: str, model: str = "gpt-4") -> int:
    """
    Count tokens accurately using tiktoken.
    
    Args:
        text: Text to count
        model: Model to use for encoding (gpt-4 is similar to Claude)
    
    Returns:
        Accurate token count
    """
    if tiktoken is None:
        # Fallback approximation
        return len(text) // 4
    
    try:
        encoding = tiktoken.encoding_for_model(model)
        tokens = encoding.encode(text)
        return len(tokens)
    except Exception:
        # Fallback if model not found
        encoding = tiktoken.get_encoding("cl100k_base")
        tokens = encoding.encode(text)
        return len(tokens)


def count_file_tokens(file_path: Path) -> dict:
    """Count tokens in a file."""
    try:
        content = file_path.read_text()
        token_count = count_tokens_accurate(content)
        
        return {
            "path": str(file_path),
            "tokens": token_count,
            "lines": content.count('\n') + 1,
            "chars": len(content),
            "efficiency": token_count / max(len(content), 1)
        }
    except Exception as e:
        return {
            "path": str(file_path),
            "error": str(e)
        }


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Count file:   python token-counter.py <file>")
        print("  Count text:   python token-counter.py -t \"your text here\"")
        print("  Count stdin:  echo \"text\" | python token-counter.py -")
        sys.exit(1)
    
    arg = sys.argv[1]
    
    # Handle different input modes
    if arg == "-t":
        # Text mode
        text = " ".join(sys.argv[2:])
        tokens = count_tokens_accurate(text)
        print(f"Tokens: {tokens:,}")
        print(f"Characters: {len(text):,}")
        print(f"Ratio: {tokens / max(len(text), 1):.3f} tokens/char")
        
    elif arg == "-":
        # Stdin mode
        text = sys.stdin.read()
        tokens = count_tokens_accurate(text)
        print(f"Tokens: {tokens:,}")
        
    else:
        # File mode
        file_path = Path(arg)
        
        if not file_path.exists():
            print(f"Error: File {file_path} does not exist")
            sys.exit(1)
        
        result = count_file_tokens(file_path)
        
        if "error" in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        
        print(f"📄 File: {result['path']}")
        print(f"🔢 Tokens: {result['tokens']:,}")
        print(f"📏 Lines: {result['lines']:,}")
        print(f"📝 Characters: {result['chars']:,}")
        print(f"⚡ Efficiency: {result['efficiency']:.3f} tokens/char")
        
        # Context size warnings
        if result['tokens'] > 10000:
            print(f"\n⚠️  Large file ({result['tokens']:,} tokens)")
            print("Consider:")
            print("  - Progressive disclosure (load sections on demand)")
            print("  - File splitting for better modularity")
            print("  - Context optimization with focused loading")


if __name__ == "__main__":
    main()

