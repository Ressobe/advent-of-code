#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int points(char first_column, char second_column) {
  if (first_column == 'A') {
    if (second_column == 'X') {
      return 3 + 1;
    }
    if (second_column == 'Y') {
      return 6 + 2;
    }
    if (second_column == 'Z') {
      return 0 + 3;
    }
  }

  if (first_column == 'B') {
    if (second_column == 'X') {
      return 0 + 1;
    }
    if (second_column == 'Y') {
      return 3 + 2;
    }
    if (second_column == 'Z') {
      return 6 + 3;
    }
  }

  if (first_column == 'C') {
    if (second_column == 'X') {
      return 6 + 1;
    }
    if (second_column == 'Y') {
      return 0 + 2;
    }
    if (second_column == 'Z') {
      return 3 + 3;
    }
  }
  return 0;
}

int points_two(char first_column, char second_column) {
  if (first_column == 'A') {
    if (second_column == 'X') {
      return 0 + 3;
    }
    if (second_column == 'Y') {
      return 3 + 1;
    }
    if (second_column == 'Z') {
      return 6 + 2;
    }
  }

  if (first_column == 'B') {
    if (second_column == 'X') {
      return 0 + 1;
    }
    if (second_column == 'Y') {
      return 3 + 2;
    }
    if (second_column == 'Z') {
      return 6 + 3;
    }
  }

  if (first_column == 'C') {
    if (second_column == 'X') {
      return 0 + 2;
    }
    if (second_column == 'Y') {
      return 3 + 3;
    }
    if (second_column == 'Z') {
      return 6 + 1;
    }
  }
  return 0;
}

int part_one(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return 1;

  char line[4];
  int suma = 0;
  while (fgets(line, sizeof(line), file)) {
    char first_column = line[0];
    char second_column = line[2];
    suma += points(first_column, second_column);
  }

  fclose(file);

  return suma;
}

int part_two(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return 1;

  char line[4];
  int suma = 0;
  while (fgets(line, sizeof(line), file)) {
    char first_column = line[0];
    char second_column = line[2];
    suma += points_two(first_column, second_column);
  }

  fclose(file);

  return suma;
}

int main() {
  printf("Part one: %d\n", part_one("dane.txt"));
  printf("Part two: %d\n", part_two("dane.txt"));
  return 0;
}
