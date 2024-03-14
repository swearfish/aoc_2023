#[cfg(test)]
mod test_extract_digits {
    use crate::extract_digits;

    #[test]
    fn test_extract_digits_only_letters() {
        let input = "abcdefg";
        let expected = "";
        assert_eq!(extract_digits(input), expected);
    }

    #[test]
    fn test_extract_digits_only_numbers() {
        let input = "123456";
        let expected = "123456";
        assert_eq!(extract_digits(input), expected);
    }

    #[test]
    fn test_extract_digits_mixed() {
        let input = "a1b2c3";
        let expected = "123";
        assert_eq!(extract_digits(input), expected);
    }

    #[test]
    fn test_extract_digits_empty_string() {
        let input = "";
        let expected = "";
        assert_eq!(extract_digits(input), expected);
    }

    #[test]
    fn test_extract_digits_special_characters() {
        let input = "!@#$%^&*()";
        let expected = "";
        assert_eq!(extract_digits(input), expected);
    }

    #[test]
    fn test_extract_digits_alphanumeric_with_spaces() {
        let input = "abc 123 xyz 456";
        let expected = "123456";
        assert_eq!(extract_digits(input), expected);
    }
}

