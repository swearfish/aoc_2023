use crate::utility::process_file;

fn form_number_from_digits(input: &str) -> Result<i32, &'static str> {
    let first_digit = input.chars().find(|c| c.is_digit(10));
    let last_digit = input.chars().rev().find(|c| c.is_digit(10));

    match (first_digit, last_digit) {
        (Some(first), Some(last)) => {
            let combined = format!("{}{}", first, last);
            combined.parse::<i32>().map_err(|_| "Failed to parse digits into an integer")
        },
        _ => Err("Did not find both a first and a last digit in the string"),
    }
}

pub fn day01_part1(filename: &str) -> i32 {
    let mut result = 0;
    let handle_line = |line: &str| {
        let num: i32 = form_number_from_digits(line).unwrap();
        result += num;
    };
    process_file(filename, handle_line);
    return result;
}

mod tests {
    #[cfg(test)]
    mod rest_form_number_from_digits {
        use crate::day01::form_number_from_digits;

        #[test]
        fn it_returns_number_for_string_with_two_digits() {
            let input = "a1b2c";
            assert_eq!(form_number_from_digits(input), Ok(12));
        }

        #[test]
        fn it_returns_error_for_string_with_no_digits() {
            let input = "abcdef";
            assert_eq!(form_number_from_digits(input), Err("Did not find both a first and a last digit in the string"));
        }

        #[test]
        fn it_returns_number_for_string_with_same_first_and_last_digit() {
            let input = "a1b2c1";
            assert_eq!(form_number_from_digits(input), Ok(11));
        }

        #[test]
        fn it_handles_large_numbers_correctly() {
            let input = "1abcdef9";
            assert_eq!(form_number_from_digits(input), Ok(19));
        }

        #[test]
        fn it_returns_error_for_empty_string() {
            let input = "";
            assert_eq!(form_number_from_digits(input), Err("Did not find both a first and a last digit in the string"));
        }
    }

    #[cfg(test)]
    mod day01_part1 {
        use crate::day01::day01_part1;

        #[test]
        fn test_example_input() {
            let filename = "res/day_01.part1.example.in";
            let result = day01_part1(filename);
            assert_eq!(result, 142);
        }

        #[test]
        fn test_puzzle_input() {
            let filename = "res/day_01.puzzle.in";
            let result = day01_part1(filename);
            assert_eq!(result, 55621);
        }
    }
}