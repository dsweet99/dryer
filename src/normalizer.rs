pub fn normalize_whitespace(input: &str) -> String {
    let mut result = String::with_capacity(input.len());
    let mut in_whitespace = false;
    let mut at_line_start = true;
    let mut last_non_space_pos = 0;

    for ch in input.chars() {
        match ch {
            '\n' => {
                trim_trailing_spaces(&mut result, last_non_space_pos);
                result.push('\n');
                last_non_space_pos = result.len();
                in_whitespace = false;
                at_line_start = true;
            }
            ' ' | '\t' | '\r' => {
                if at_line_start {
                    continue;
                }
                if !in_whitespace {
                    result.push(' ');
                    in_whitespace = true;
                }
            }
            _ => {
                result.push(ch);
                last_non_space_pos = result.len();
                in_whitespace = false;
                at_line_start = false;
            }
        }
    }

    trim_trailing_spaces(&mut result, last_non_space_pos);
    result
}

fn trim_trailing_spaces(s: &mut String, last_non_space_pos: usize) {
    s.truncate(last_non_space_pos);
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_collapse_spaces() {
        assert_eq!(normalize_whitespace("a    b"), "a b");
    }

    #[test]
    fn test_trim_leading() {
        assert_eq!(normalize_whitespace("   hello"), "hello");
    }

    #[test]
    fn test_trim_trailing() {
        assert_eq!(normalize_whitespace("hello   "), "hello");
    }

    #[test]
    fn test_multiline() {
        let input = "  foo   bar  \n   baz   ";
        let expected = "foo bar\nbaz";
        assert_eq!(normalize_whitespace(input), expected);
    }

    #[test]
    fn test_tabs() {
        assert_eq!(normalize_whitespace("a\t\tb"), "a b");
    }
}
