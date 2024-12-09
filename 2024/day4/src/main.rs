use std::fs::File;
use std::io::{self, BufRead};

const LETTERS: [char; 3] = ['M', 'A', 'S'];

fn check_top(char_matrix: &[Vec<char>], i: usize, j: usize, amount_of_letters: usize) -> bool {
    let mut k: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i - k][j] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
    }
    is_match
}

fn check_down(char_matrix: &[Vec<char>], i: usize, j: usize, amount_of_letters: usize) -> bool {
    let mut k: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i + k][j] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
    }
    is_match
}

fn check_left(char_matrix: &[Vec<char>], i: usize, j: usize, amount_of_letters: usize) -> bool {
    let mut k: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i][j - k] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
    }
    is_match
}

fn check_right(char_matrix: &[Vec<char>], i: usize, j: usize, amount_of_letters: usize) -> bool {
    let mut k: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i][j + k] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
    }
    is_match
}

fn check_left_top_corner(
    char_matrix: &[Vec<char>],
    i: usize,
    j: usize,
    amount_of_letters: usize,
) -> bool {
    let mut k: usize = 1;
    let mut l: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i - l][j - k] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
        l += 1;
    }
    is_match
}

fn check_right_top_corner(
    char_matrix: &[Vec<char>],
    i: usize,
    j: usize,
    amount_of_letters: usize,
) -> bool {
    let mut k: usize = 1;
    let mut l: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i - l][j + k] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
        l += 1;
    }
    is_match
}

fn check_left_down_corner(
    char_matrix: &[Vec<char>],
    i: usize,
    j: usize,
    amount_of_letters: usize,
) -> bool {
    let mut k: usize = 1;
    let mut l: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i + l][j - k] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
        l += 1;
    }
    is_match
}

fn check_right_down_corner(
    char_matrix: &[Vec<char>],
    i: usize,
    j: usize,
    amount_of_letters: usize,
) -> bool {
    let mut k: usize = 1;
    let mut l: usize = 1;
    let mut is_match = true;
    while k <= amount_of_letters {
        if char_matrix[i + l][j + k] != LETTERS[k - 1] {
            is_match = false;
        }
        k += 1;
        l += 1;
    }
    is_match
}

fn check(
    char_matrix: &[Vec<char>],
    amount_of_rows: usize,
    amount_of_columns: usize,
    i: usize,
    j: usize,
) -> i32 {
    let amount_of_letters = 3;
    let mut matches_sum = 0;

    if i >= amount_of_letters && check_top(char_matrix, i, j, amount_of_letters) {
        matches_sum += 1
    };

    if amount_of_rows - i > amount_of_letters && check_down(char_matrix, i, j, amount_of_letters) {
        matches_sum += 1;
    };

    if j >= amount_of_letters && check_left(char_matrix, i, j, amount_of_letters) {
        matches_sum += 1;
    }

    if amount_of_columns - j > amount_of_letters
        && check_right(char_matrix, i, j, amount_of_letters)
    {
        matches_sum += 1;
    }

    if j >= amount_of_letters
        && i >= amount_of_letters
        && check_left_top_corner(char_matrix, i, j, amount_of_letters)
    {
        matches_sum += 1;
    }

    if amount_of_columns - j > amount_of_letters
        && i >= amount_of_letters
        && check_right_top_corner(char_matrix, i, j, amount_of_letters)
    {
        matches_sum += 1;
    }

    if j >= amount_of_letters
        && amount_of_rows - i > amount_of_letters
        && check_left_down_corner(char_matrix, i, j, amount_of_letters)
    {
        matches_sum += 1;
    }

    if amount_of_columns - j > amount_of_letters
        && amount_of_rows - i > amount_of_letters
        && check_right_down_corner(char_matrix, i, j, amount_of_letters)
    {
        matches_sum += 1;
    }

    matches_sum
}

fn part_one() -> io::Result<()> {
    let file = File::open("plik.txt")?;

    let mut char_matrix: Vec<Vec<char>> = Vec::new();
    let reader = io::BufReader::new(file);
    for line_result in reader.lines() {
        let line = line_result?;
        let chars: Vec<char> = line.chars().collect();
        char_matrix.push(chars);
    }

    let amount_of_rows = char_matrix.len();
    let amount_of_columns = char_matrix.first().map_or(0, |row| row.len());

    let mut sum = 0;
    for (i, row) in char_matrix.iter().enumerate() {
        for (j, column) in row.iter().enumerate() {
            if column == &'X' {
                sum += check(&char_matrix, amount_of_rows, amount_of_columns, i, j);
            }
        }
    }
    println!("{}", sum);

    Ok(())
}

fn check_part_two_1(char_matrix: &[Vec<char>], i: usize, j: usize) -> bool {
    if char_matrix[i - 1][j - 1] == 'M'
        && char_matrix[i - 1][j + 1] == 'M'
        && char_matrix[i + 1][j - 1] == 'S'
        && char_matrix[i + 1][j + 1] == 'S'
    {
        return true;
    }
    false
}

fn check_part_two_2(char_matrix: &[Vec<char>], i: usize, j: usize) -> bool {
    if char_matrix[i - 1][j - 1] == 'S'
        && char_matrix[i - 1][j + 1] == 'M'
        && char_matrix[i + 1][j - 1] == 'S'
        && char_matrix[i + 1][j + 1] == 'M'
    {
        return true;
    }
    false
}

fn check_part_two_3(char_matrix: &[Vec<char>], i: usize, j: usize) -> bool {
    if char_matrix[i - 1][j - 1] == 'S'
        && char_matrix[i - 1][j + 1] == 'S'
        && char_matrix[i + 1][j - 1] == 'M'
        && char_matrix[i + 1][j + 1] == 'M'
    {
        return true;
    }
    false
}

fn check_part_two_4(char_matrix: &[Vec<char>], i: usize, j: usize) -> bool {
    if char_matrix[i - 1][j - 1] == 'M'
        && char_matrix[i - 1][j + 1] == 'S'
        && char_matrix[i + 1][j - 1] == 'M'
        && char_matrix[i + 1][j + 1] == 'S'
    {
        return true;
    }
    false
}

fn part_two() -> io::Result<()> {
    let file = File::open("plik.txt")?;

    let mut char_matrix: Vec<Vec<char>> = Vec::new();
    let reader = io::BufReader::new(file);
    for line_result in reader.lines() {
        let line = line_result?;
        let chars: Vec<char> = line.chars().collect();
        char_matrix.push(chars);
    }

    let amount_of_rows = char_matrix.len();
    let amount_of_columns = char_matrix.first().map_or(0, |row| row.len());

    let mut sum = 0;
    for (i, row) in char_matrix.iter().enumerate() {
        for (j, column) in row.iter().enumerate() {
            if column == &'A'
                && i >= 1
                && i < amount_of_rows - 1
                && j >= 1
                && j < amount_of_columns - 1
                && (check_part_two_1(&char_matrix, i, j)
                    || check_part_two_2(&char_matrix, i, j)
                    || check_part_two_3(&char_matrix, i, j)
                    || check_part_two_4(&char_matrix, i, j))
            {
                sum += 1;
            }
        }
    }
    println!("{}", sum);

    Ok(())
}

fn main() {
    let _ = part_two();
}
