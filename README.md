# dryer
Duplicate code detector

- Finds clusters of two or more nearly-matching substrings in a code base
- Language-agnostic
- Designed for LLM-in-the-loop coding: fast, actionable, concise feedback
- No training; always ready to run
- Free


## Usage
```
# Check all Python files
dryer -e py .
```

```
# Check all Rust files, show verbose output
dryer -e rs -v .
```

- respects .gitignore
- recursive

  
