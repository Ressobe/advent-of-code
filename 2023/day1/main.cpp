#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>
#include <tuple>


void part_one() {
  std::ifstream inputFile("input.txt");

  if (!inputFile.is_open()) {
    return;
  }
  std::stringstream buffer;

  buffer << inputFile.rdbuf(); 

  inputFile.close();    
  std::string fileContent = buffer.str();


  int suma = 0;

  std::vector<char> charNumbers;

  for (int i = 0; i < fileContent.size(); i++) {
    if (fileContent[i] == '\n') {
      std::string n;
      n += charNumbers[0];
      n += charNumbers[charNumbers.size() - 1];
      suma += std::stoi(n);
      charNumbers.clear();
      continue;
    }

    if (std::isdigit(fileContent[i])) {
      charNumbers.push_back(fileContent[i]);
    }
  }

  std::cout << suma;
}



void part_two() {
  std::unordered_map<std::string, int> digits = {
    {"one", 1},
    {"two", 2},
    {"three", 3},
    {"four", 4},
    {"five", 5},
    {"six", 6},
    {"seven", 7},
    {"eight", 8},
    {"nine", 9},
  };

  std::ifstream inputFile("input.txt");

  std::vector<std::string> lines;
  std::string l;

  while (std::getline(inputFile, l)) {
      lines.push_back(l);
  }
  inputFile.close();

  int sum = 0;
  
  std::vector<std::tuple<int, int>> numberPosistions;

  for (const auto& str : lines) {

      for (const auto& item: digits)  {
        size_t find = str.find(item.first);
        if (find != std::string::npos) {
          int first = find;
          int last = first + (str.size() - 1);
          numberPosistions.push_back(std::make_tuple(first, last));
        }
      }

      for (int i = 0; i < str.size(); i++) {
        if (std::isdigit(str[i])) {
          numberPosistions.push_back(std::make_tuple(i, i));
        }
      }
  }
}



int main() {
  std::cout << "Part one: " << std::endl;
  part_one();
  std::cout << "Part two: " << std::endl;
  part_two();

  return 0;
}
