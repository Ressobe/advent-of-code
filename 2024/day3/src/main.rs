use regex::Regex;
use std::fs::File;
use std::io::{self, BufRead};

fn part_one() -> io::Result<()> {
    let file = File::open("plik.txt")?;
    let re = Regex::new(r"mul\((\d+),(\d+)\)").unwrap();

    let reader = io::BufReader::new(file);
    let mut sum = 0;
    for line_result in reader.lines() {
        let line = match line_result {
            Ok(line) => line,
            Err(e) => {
                eprintln!("Błąd odczytu linii: {}", e);
                continue;
            }
        };
        for cap in re.captures_iter(&line) {
            let num1: i32 = cap[1].parse().unwrap();
            let num2: i32 = cap[2].parse().unwrap();
            sum += num1 * num2;
        }
    }
    println!("Part one: {}", sum);

    Ok(())
}

fn part_two() -> io::Result<()> {
    let file = File::open("plik.txt")?;
    let re = Regex::new(r"(mul\((\d+),(\d+)\)|don't\(\)|do\(\))").unwrap();

    let reader = io::BufReader::new(file);
    let mut sum = 0;
    let mut enable = true;
    for line_result in reader.lines() {
        let line = match line_result {
            Ok(line) => line,
            Err(e) => {
                eprintln!("Błąd odczytu linii: {}", e);
                continue;
            }
        };
        for cap in re.captures_iter(&line) {
            let full_match = cap.get(0).map_or("", |m| m.as_str());
            if full_match.starts_with("mul") {
                let num1: i32 = cap[2].parse().unwrap();
                let num2: i32 = cap[3].parse().unwrap();
                if enable {
                    sum += num1 * num2;
                }
            } else if full_match == "don't()" {
                enable = false;
            } else if full_match == "do()" {
                enable = true;
            }
        }
    }
    println!("Part two: {}", sum);

    Ok(())
}

fn main() {
    let _ = part_two();
}
