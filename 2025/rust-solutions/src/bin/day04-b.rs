use std::fs;

fn main() {
    // const PUZZLE_FILENAME: &str = "inputs/day04/example-input.txt";
    const PUZZLE_FILENAME: &str = "inputs/day04/puzzle-input.txt";

    let data = fs::read_to_string(PUZZLE_FILENAME).expect("Should be able to read input file");

    println!("{}", solve(data));
}

fn solve(data: String) -> u32 {
    let mut lines: Vec<String> = data.lines().map(|s| s.to_string()).collect();

    let mut res = 0;

    loop {
        let papers_removed = remove_papers(&mut lines);
        if papers_removed == 0 {
            break;
        }

        res += papers_removed;
    }

    res
}

/// Returns the number of papers removed
fn remove_papers(map: &mut Vec<String>) -> u32 {
    let original_map = map.clone();
    let mut sum = 0;

    for x in 0..original_map.get(0).unwrap().len() {
        for y in 0..original_map.len() {
            if can_paper_be_accessed(&original_map, x as i32, y as i32) {
                sum += 1;
                map.get_mut(y).unwrap().replace_range(x..x + 1, ".");
            }
        }
    }

    sum
}

fn can_paper_be_accessed(map: &[String], x: i32, y: i32) -> bool {
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

fn is_paper_at(map: &[String], x: i32, y: i32) -> bool {
    let line = match map.get(y as usize) {
        Some(line) => line,
        None => return false,
    };

    match line.chars().nth(x as usize) {
        Some(ch) => ch == '@',
        None => false,
    }
}
