use std::fs::File;
use std::io::{self, BufRead};

fn process_strings<S, I, F>(strings: I, mut action: F)
    where
        S: AsRef<str>,
        I: IntoIterator<Item = S>,
        F: FnMut(&str),
{
    for s in strings {
        action(s.as_ref());
    }
}

pub fn process_file<F>(filename: &str, action: F) where F: FnMut(&str) {
    let file = File::open(filename).unwrap();
    let reader = io::BufReader::new(file);
    process_strings(reader.lines().filter_map(Result::ok), action);
}
