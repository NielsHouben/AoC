use std::{cmp, fs};

/*
    IDEA:
    1. iterate from right (except last) if n bigger than found, set n as first_digit
        during this keep track of next-biggest
*/

fn main() {
    const PUZZLE_FILENAME: &str = "inputs/day03/puzzle-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    let mut val1: u32;
    let mut val2: u32;
    let mut potential_val2: u32;
    let mut res: u32 = 0;

    for line in data.split("\n") {
        val1 = 0;
        val2 = 0;
        potential_val2 = 0;
        let mut iter = line.chars().rev();
        let Some(last) = iter.next() else {
            continue;
        };

        let last = last.to_digit(10).expect("Only digits in input");

        for character in iter {
            let digit = character.to_digit(10).expect("Only digits in input");
            if digit > val1 {
                val2 = val1;
                val1 = digit;
            } else if digit > val2 {
                potential_val2 = digit;
            }
            if digit == val1 {
                val2 = cmp::max(val2, potential_val2);
            }
        }

        val2 = cmp::max(val2, last);

        let mut o: String = "".to_owned();
        o.push_str(val1.to_string().as_str());
        o.push_str(val2.to_string().as_str());

        res += o.parse::<u32>().unwrap();
    }

    println!("{}", res);
}
