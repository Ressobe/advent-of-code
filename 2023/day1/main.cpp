#include <cstdlib>
#include <iostream>
#include <fstream>


void part_one() {
  std::ifstream inputFile("input.txt");

  if (!inputFile.is_open()) {
    return;
  }

  std::string line;

  int sum = 0;
  while (std::getline(inputFile, line)) {
    char leftMost = ' ';
    char rightMost = ' ';

    for (char& c : line) {

      if (std::isdigit(c)) {
        if (leftMost == ' ') {
          leftMost = c;
          rightMost = c;
        } else {
          rightMost = c;
        }
      }

    }

    std::cout << leftMost << rightMost << std::endl;
    
    std::string number;
    number += leftMost;
    number += rightMost;
    
    sum += std::atoi(number.c_str());
  }

  inputFile.close();

  std::cout << sum << std::endl;
}


int match_digits(std::string input) {
  const char* digits[9] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
  for (int i = 0; i < 9; i++) {
    if (input.find(digits[i]) != std::string::npos) {
      return i + 1;
    }
  }
  return -1;
}


void part_two() {
  std::ifstream inputFile("input.txt");

  if (!inputFile.is_open()) {
    return;
  }

  std::string line;

  int sum = 0;
  while (std::getline(inputFile, line)) {
    char leftMost = ' ';
    char rightMost = ' ';

    std::string currentString = "";

    for (char& c : line) {
      currentString += c;
      int r = match_digits(currentString);

      if (r != -1) {
          if (leftMost == ' ') {
            leftMost = '0' + r;
            rightMost = '0' + r;
          } else {
            rightMost = '0' + r;
          }

        currentString = "";
        currentString += c;

      } else {
        if (std::isdigit(c)) {
          if (leftMost == ' ') {
            leftMost = c;
            rightMost = c;
          } else {
            rightMost = c;
          }
        }
      }
    }
    
    std::string number;
    number += leftMost;
    number += rightMost;
    
    sum += std::atoi(number.c_str());
  }

  inputFile.close();

  std::cout << sum << std::endl;
}



int main() {
  // std::cout << "Part one: " << std::endl;
  //
  // part_one();
  std::cout << "Part two: " << std::endl;
  part_two();

  return 0;
}
