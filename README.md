# dryer
*Warning: Code may shrink in dryer*

- Finds clusters of two or more nearly-matching substrings in a code base
- Language-agnostic
- Designed for LLM-in-the-loop coding: fast, actionable, concise feedback
- No training; always ready to run
- Free

## Installation
```
cargo install dryer
```


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

  
