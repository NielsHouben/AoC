use std::{cmp, fs, ops::RangeInclusive};

fn main() {
    // const PUZZLE_FILENAME: &str = "inputs/day05/example-input.txt";
    const PUZZLE_FILENAME: &str = "inputs/day05/puzzle-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    println!("{}", solve(&data));
}

fn solve(data: &str) -> u64 {
    let mut lines = data.lines();

    let mut ranges: Vec<RangeInclusive<u64>> = [].to_vec();

    let mut smallest: u64 = u64::MAX;

    while let Some(line) = lines.next() {
        if line.is_empty() {
            break;
        }

        let (first, second) = line.split_once("-").unwrap();

        let start: u64 = first.parse().unwrap();
        let end: u64 = second.parse().unwrap();

        smallest = cmp::min(smallest, start);

        ranges.push(start..=end);
    }

    let mut res: u64 = 0;

    ranges.sort_by_key(|range| *range.start());

    let mut pos = smallest;

    for range in ranges {
        let delta = go_with_range(&mut pos, &range);
        res += delta;
    }

    res
}

/// Returns the number of steps it took within the range
fn go_with_range(pos: &mut u64, range: &RangeInclusive<u64>) -> u64 {
    if *pos > *range.end() {
        return 0;
    }

    let steps_taken = range.end() - cmp::max(*pos, *range.start()) + 1;
    *pos = range.end() + 1;

    steps_taken
}
