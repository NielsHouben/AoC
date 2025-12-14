use std::{fs, ops::RangeInclusive};

fn main() {
    // const PUZZLE_FILENAME: &str = "inputs/day05/example-input.txt";
    const PUZZLE_FILENAME: &str = "inputs/day05/puzzle-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    println!("{}", solve(&data));
}

fn solve(data: &str) -> u64 {
    let mut lines = data.lines();

    let mut ranges: Vec<RangeInclusive<u64>> = [].to_vec();

    while let Some(line) = lines.next() {
        if line.is_empty() {
            break;
        }

        let (first, second) = line.split_once("-").unwrap();

        let start: u64 = first.parse().unwrap();
        let end: u64 = second.parse().unwrap();

        ranges.push(start..=end);
    }

    let mut res = 0;
    for line in lines {
        let num = line.parse().unwrap();
        if is_in_one_of_ranges(num, &ranges) {
            res += 1;
        }
    }

    res
}

fn is_in_one_of_ranges(num: u64, ranges: &[RangeInclusive<u64>]) -> bool {
    for range in ranges {
        if range.contains(&num) {
            return true;
        }
    }
    false
}
