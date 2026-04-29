pub struct Linter {
    error: Option<String>,
    stack: Vec<char>,
}

impl Linter {
    pub fn new() -> Self {
        Self {
            error: None,
            stack: Vec::new(),
        }
    }

    pub fn lint(&mut self, text: &str) -> Result<(), String> {
        self.stack.clear();
        self.error = None;

        for (_, char) in text.chars().enumerate() {
            if self.is_opening_brace(char) {
                self.stack.push(char);
            } else if self.is_closing_brace(char) {
                if self.stack.is_empty() {
                    self.error = Some(format!("{} does not have a corresponding opening brace", char));
                    return Err(self.error.clone().unwrap());
                }

                if !self.closes_most_recent_opening_brace(char) {
                    self.error = Some(format!("{} has no corresponding opening brace", char));
                    return Err(self.error.clone().unwrap());
                }

                self.stack.pop();
            }
        }

        if !self.stack.is_empty() {
            let last_opening = self.stack.last().unwrap();
            self.error = Some(format!("{} does not have a closing brace", last_opening));
            return Err(self.error.clone().unwrap());
        }

        Ok(())
    }

    pub fn get_error(&self) -> Option<&String> {
        self.error.as_ref()
    }

    fn is_opening_brace(&self, char: char) -> bool {
        matches!(char, '(' | '[' | '{')
    }

    fn is_closing_brace(&self, char: char) -> bool {
        matches!(char, ')' | ']' | '}')
    }

    fn opening_brace_of(&self, char: char) -> Option<char> {
        match char {
            ')' => Some('('),
            ']' => Some('['),
            '}' => Some('{'),
            _ => None,
        }
    }

    fn most_recent_opening_brace(&self) -> Option<char> {
        self.stack.last().copied()
    }

    fn closes_most_recent_opening_brace(&self, char: char) -> bool {
        if let Some(opening_brace) = self.opening_brace_of(char) {
            if let Some(most_recent) = self.most_recent_opening_brace() {
                return opening_brace == most_recent;
            }
        }
        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_valid_braces() {
        let mut linter = Linter::new();
        assert!(linter.lint("()").is_ok());
        assert!(linter.lint("[]").is_ok());
        assert!(linter.lint("{}").is_ok());
        assert!(linter.lint("({[]})").is_ok());
        assert!(linter.lint("function() { return [1, 2, 3]; }").is_ok());
    }

    #[test]
    fn test_invalid_braces() {
        let mut linter = Linter::new();
        
        // Missing closing brace
        assert!(linter.lint("(").is_err());
        assert_eq!(linter.get_error(), Some(&"( does not have a closing brace".to_string()));
        
        // Missing opening brace
        assert!(linter.lint(")").is_err());
        assert_eq!(linter.get_error(), Some(&") does not have a corresponding opening brace".to_string()));
        
        // Mismatched braces
        assert!(linter.lint("([)]").is_err());
        assert_eq!(linter.get_error(), Some(&") has no corresponding opening brace".to_string()));
    }
}