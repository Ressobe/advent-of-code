use std::fs::File;
use std::io::{self, BufRead};

fn parse_pair(line: &str) -> Option<(i32, i32)> {
    let mut parts = line.split("|");
    let first_number = parts.next()?.parse::<i32>().ok();
    let second_number = parts.next()?.parse::<i32>().ok();

    match (first_number, second_number) {
        (Some(a), Some(b)) => Some((a, b)),
        _ => None,
    }
}

fn parse_numbers(line: &str) -> Vec<i32> {
    line.split(',')
        .filter_map(|num| num.trim().parse::<i32>().ok())
        .collect()
}

type NumbersVec = Vec<(i32, i32)>;
type RulesVec = Vec<Vec<i32>>;

fn read_file() -> io::Result<(NumbersVec, RulesVec)> {
    let file = File::open("plik.txt")?;

    let mut numbers: Vec<(i32, i32)> = Vec::new();
    let mut rules: Vec<Vec<i32>> = Vec::new();
    let mut is_parsing_pairs = true;

    let reader = io::BufReader::new(file);
    for line_result in reader.lines() {
        let line = line_result.unwrap();

        if line.trim().is_empty() {
            is_parsing_pairs = false;
            continue;
        }

        if is_parsing_pairs {
            match parse_pair(&line) {
                Some(tuple) => {
                    numbers.push(tuple);
                }
                None => {
                    eprintln!("Błąd podczas parsowania par {}", line);
                }
            }
        }

        if !is_parsing_pairs {
            let numbers = parse_numbers(&line);
            rules.push(numbers);
        }
    }

    Ok((numbers, rules))
}

fn check_pair(left_number: &i32, right_number: &i32, numbers: &NumbersVec) -> bool {
    let mut is_pair_exist = false;
    for pair in numbers {
        if left_number == &pair.0 && right_number == &pair.1 {
            is_pair_exist = true;
        }
    }
    is_pair_exist
}

fn part_one(numbers: &NumbersVec, rules: &RulesVec) {
    let mut sum = 0;
    for rule in rules.iter() {
        let mut is_update_correct = true;
        for (i, first_number) in rule.iter().enumerate() {
            let mut is_correct = true;

            for (j, second_number) in rule.iter().enumerate() {
                if i == j {
                    continue;
                }
                if i > j {
                    is_correct = check_pair(second_number, first_number, numbers);
                }
                if i < j {
                    is_correct = check_pair(first_number, second_number, numbers);
                }
                if !is_correct {
                    break;
                }
            }
            if !is_correct {
                is_update_correct = false;
                break;
            }
        }

        if is_update_correct {
            let middle = rule.get(rule.len() / 2).unwrap();
            sum += middle;
        }
    }
    println!("{}", sum);
}

fn check(rule: &mut Vec<i32>, numbers: &NumbersVec, swapped: &mut bool) {
    for i in 0..rule.len() {
        let first_number = rule[i];
        let mut is_correct = true;

        for j in 0..rule.len() {
            let second_number = rule[j];
            if i == j {
                continue;
            }

            if i > j {
                is_correct = check_pair(&first_number, &second_number, numbers);
            }
            if i < j {
                is_correct = check_pair(&second_number, &first_number, numbers);
            }

            if is_correct {
                rule.swap(i, j);
                break;
            }
        }
        if is_correct {
            *swapped = true;
            check(rule, numbers, swapped);
        }
    }
}

fn part_two(numbers: &NumbersVec, rules: &mut RulesVec) {
    let mut sum = 0;
    for rule in rules.iter_mut() {
        let mut swapped = false;

        check(rule, numbers, &mut swapped);

        if swapped {
            let middle = rule.get(rule.len() / 2).unwrap();
            sum += middle;
        }
    }
    println!("{}", sum);
}

fn main() {
    let (numbers, mut rules) = match read_file() {
        Ok((numbers, rules)) => (numbers, rules),
        Err(e) => {
            eprintln!("Błąd podczas wczytywania pliku: {}", e);
            return;
        }
    };

    // part_one(&numbers, &rules);
    part_two(&numbers, &mut rules);
}
