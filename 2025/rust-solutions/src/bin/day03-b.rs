use std::fs;

/*
    IDEA:
    1. iterate from right (except last) if n bigger than found, set n as first_digit
        during this keep track of next-biggest
*/

const NUMBER_OF_DIGITS: u32 = 12;

fn main() {
    const PUZZLE_FILENAME: &str = "inputs/day03/puzzle-input.txt";
    // const PUZZLE_FILENAME: &str = "inputs/day03/example-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    println!("{}", sum_of_largets_joltages(data));
}

fn sum_of_largets_joltages(data: String) -> u64 {
    let mut res: u64 = 0;

    for line in data.split("\n") {
        if line.len() == 0 {
            continue;
        }
        res += largest_joltage(line);
    }

    res
}

fn largest_joltage(bank: &str) -> u64 {
    let mut val1: u32;
    let mut index: usize = 0;
    let mut num: u64 = 0;

    for nth_digit in 0..12 {
        (index, val1) = largest_digit(bank, index, nth_digit);
        index += 1;
        num += val1 as u64 * 10_u64.pow(NUMBER_OF_DIGITS - nth_digit - 1);
    }

    num
}

fn largest_digit(choices: &str, start: usize, nth_digit: u32) -> (usize, u32) {
    assert!(nth_digit < NUMBER_OF_DIGITS);
    let mut largest = '0';
    let mut largest_index: usize = 0;

    let end: usize = choices.len() - NUMBER_OF_DIGITS as usize + 1 + nth_digit as usize;
    for i in start..end {
        let character = choices.chars().nth(i).unwrap();
        if largest < character {
            largest = character;
            largest_index = i;
        }
    }

    (
        largest_index,
        largest.to_digit(10).expect("Only digits in input"),
    )
}
