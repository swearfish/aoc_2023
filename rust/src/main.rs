mod tests;
mod utility;
mod day01;

use std::io;
use crate::day01::day01_part1;

fn extract_digits(input: &str) -> String {
    input.chars().filter(|c| c.is_numeric()).collect()
}

fn main() -> io::Result<()> {
    let filename = "res/day_01.puzzle.in";
    let result = day01_part1(filename);
    println!("{}", result);

    Ok(())
}

