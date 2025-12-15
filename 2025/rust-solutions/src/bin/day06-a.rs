use std::{cmp, fs};

fn main() {
    // const PUZZLE_FILENAME: &str = "inputs/day06/example-input.txt";
    const PUZZLE_FILENAME: &str = "inputs/day06/puzzle-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    println!("{}", solve(&data));
}

fn solve(data: &str) -> u64 {
    let mut lines = data.lines().peekable();

    let mut problem_values: Vec<Vec<u64>> = vec![];
    let mut operators: Vec<&str> = vec![];

    while let Some(line) = lines.next() {
        // If we are at the last.
        if lines.peek().is_none() {
            operators.extend(line.split_whitespace());
            break;
        }

        let numbers = line.split_whitespace();

        let mut values: Vec<u64> = vec![];
        for number in numbers {
            let n: u64 = if let Ok(n) = number.parse() {
                n
            } else {
                break;
            };
            values.push(n);
        }

        problem_values.push(values);
    }

    let mut total = 0;
    for (i, operator) in operators.iter().enumerate() {
        let mut res: u64 = 0;
        for val in &problem_values {
            res = match *operator {
                "*" => cmp::max(res, 1) * val.get(i).unwrap(),
                "+" => res + val.get(i).unwrap(),
                _ => 0,
            }
        }
        total += res;
    }

    total
}
