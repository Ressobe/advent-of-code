use std::collections::HashSet;
use std::fs::File;
use std::io::{self, BufRead};

type PuzzleMap = Vec<Vec<char>>;

fn read_file() -> io::Result<PuzzleMap> {
    let file = File::open("plik.txt")?;

    let reader = io::BufReader::new(file);
    let mut map: Vec<Vec<char>> = Vec::new();
    for line_result in reader.lines() {
        let line = line_result.unwrap();
        let chars: Vec<char> = line.chars().collect();
        map.push(chars);
    }

    Ok(map)
}

fn part_one(map: &PuzzleMap) {
    let mut guard_position: (usize, usize) = (0, 0);

    for (i, row) in map.iter().enumerate() {
        for (j, &cell) in row.iter().enumerate() {
            if cell == '>' || cell == 'v' || cell == '<' || cell == '^' {
                guard_position = (i, j);
                break;
            }
        }
    }

    let directions: [(i32, i32); 4] = [(0, 1), (1, 0), (0, -1), (-1, 0)];
    let mut unique_positions: HashSet<(usize, usize)> = HashSet::new();
    let mut i = guard_position.0;
    let mut j = guard_position.1;

    let mut current_direction = match map[i][j] {
        '>' => 0,
        'v' => 1,
        '<' => 2,
        '^' => 3,
        _ => unreachable!(),
    };

    while i < map.len() && j < map[0].len() {
        unique_positions.insert((i, j));

        let mut new_i = i as i32 + directions[current_direction].0;
        let mut new_j = j as i32 + directions[current_direction].1;

        if new_i < 0 || new_j < 0 || new_i >= map.len() as i32 || new_j >= map[0].len() as i32 {
            break;
        }

        if map[new_i as usize][new_j as usize] == '#' {
            current_direction = (current_direction + 1) % 4;
            new_i = i as i32 + directions[current_direction].0;
            new_j = j as i32 + directions[current_direction].1;
        }

        i = new_i as usize;
        j = new_j as usize;
    }

    println!("{}", unique_positions.len());
}

fn main() {
    let map = match read_file() {
        Ok(map) => map,
        Err(e) => {
            eprintln!("Błąd podczas wczytywania pliku: {}", e);
            return;
        }
    };
    part_one(&map);
}
