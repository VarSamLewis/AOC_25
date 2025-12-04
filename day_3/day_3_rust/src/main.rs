use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn fileread<P>(filename: P) -> io::Result<Vec<String>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    let lines = io::BufReader::new(file).lines();
    let content: Vec<String> = lines.collect::<Result<_, _>>()?;
    Ok(content)
}

fn extract_two_highest_nums(line: &str) -> u32 {
    let chars: Vec<char> = line.chars().collect();

    // Find the max character and its index
    let max_char = chars.iter().max().unwrap();
    let first_idx = chars.iter().position(|&c| c == *max_char).unwrap();

    if first_idx < chars.len() - 1 {
        // Get max from remaining part after first_idx
        let second = chars[first_idx + 1..].iter().max().unwrap();
        let result = format!("{}{}", max_char, second);
        return result.parse().unwrap();
    } else {
        // Get unique chars and sort in reverse
        let mut unique_chars: Vec<char> = chars.iter().cloned().collect();
        unique_chars.sort_by(|a, b| b.cmp(a)); // reverse sort
        unique_chars.dedup(); // remove duplicates

        if unique_chars.len() >= 2 {
            let max_digit = unique_chars[0];
            let second_max = unique_chars[1];
            let result = format!("{}{}", second_max, max_digit);
            return result.parse().unwrap();
        } else {
            let result = format!("{}{}", chars[0], chars[1]);
            return result.parse().unwrap();
        }
    }
}

fn main() {
    let filename = "input.txt";
    let content = fileread(filename).expect("Failed to read file");

    let mut total_sum = 0;

    for line in &content {
        let result = extract_two_highest_nums(line);
        total_sum += result;
    }

    println!("Total sum: {}", total_sum);
}
