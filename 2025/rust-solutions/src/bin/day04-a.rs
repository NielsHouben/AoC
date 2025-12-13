use std::fs;

fn main() {
    // const PUZZLE_FILENAME: &str = "inputs/day04/example-input.txt";
    const PUZZLE_FILENAME: &str = "inputs/day04/puzzle-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    println!("{}", solve(&data));
}

fn solve(data: &str) -> u32 {
    let lines: Vec<&str> = data.lines().collect();

    for line in &lines {
        println!("{}", line);
    }

    let mut sum = 0;

    for x in 0..lines.get(0).unwrap().len() {
        for y in 0..lines.len() {
            if can_paper_be_accessed(&lines, x as i32, y as i32) {
                sum += 1;
            }
        }
    }

    sum
}

fn can_paper_be_accessed(map: &[&str], x: i32, y: i32) -> bool {
    if !is_paper_at(map, x, y) {
        return false;
    }

    let above = [
        is_paper_at(map, x - 1, y - 1),
        is_paper_at(map, x, y - 1),
        is_paper_at(map, x + 1, y - 1),
    ];
    let sides = [is_paper_at(map, x - 1, y), is_paper_at(map, x + 1, y)];
    let below = [
        is_paper_at(map, x - 1, y + 1),
        is_paper_at(map, x, y + 1),
        is_paper_at(map, x + 1, y + 1),
    ];

    let paper_count = above
        .iter()
        .chain(sides.iter())
        .chain(below.iter())
        .filter(|&&b| b)
        .count();

    paper_count < 4
}

fn is_paper_at(map: &[&str], x: i32, y: i32) -> bool {
    let line = match map.get(y as usize) {
        Some(line) => line,
        None => return false,
    };

    match line.chars().nth(x as usize) {
        Some(ch) => ch == '@',
        None => false,
    }
}
