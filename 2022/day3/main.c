#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int priority(char left_side[], char right_side[], int len) {
  for (int i = 0; i < len; i++) {
    for (int j = 0; j < len; j++)
      if (left_side[i] == right_side[j]) {
        int ascii = (int)(left_side[i]);
        if (ascii >= 97) {
          return ascii - 96;
        } else {
          return ascii - 38;
        }
      }
  }
  return 0;
}

int priority2(char first_line[], char second_line[], char third_line[],
              int first_len, int second_len, int third_len) {
  for (int i = 0; i < first_len; i++) {
    for (int j = 0; j < second_len; j++)
      for (int k = 0; k < third_len; k++) {

        if (first_line[i] == second_line[j] && first_line[i] == third_line[k]) {
          int ascii = (int)(first_line[i]);

          if (ascii >= 97) {
            return ascii - 96;
          } else {
            return ascii - 38;
          }
        }
      }
  }
  return 0;
}

int part_one(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return 1;

  char line[100];
  int suma = 0;
  while (fgets(line, sizeof(line), file)) {

    int len = strlen(line) - 1;
    int half = len / 2;
    char *left_side = (char *)malloc(half + 1 * sizeof(char));
    char *right_side = (char *)malloc(half + 1 * sizeof(char));

    int i;
    for (i = 0; i < half; i++) {
      left_side[i] = line[i];
    }
    left_side[half] = '\0';

    int j = i;
    for (int k = 0; k < half; k++) {
      right_side[k] = line[j];
      j++;
    }
    right_side[half] = '\0';

    suma += priority(left_side, right_side, half);

    free(left_side);
    free(right_side);
  }

  fclose(file);

  return suma;
}

int part_two(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return 1;

  char line[100];
  int suma = 0;

  char first_line[100];
  char second_line[100];
  char third_line[100];

  int first_line_len;
  int second_line_len;
  int third_line_len;

  int i = 1;
  while (fgets(line, sizeof(line), file)) {

    int len = strlen(line) - 1;

    if (i == 1) {
      first_line_len = len;
      for (int j = 0; j < len; j++) {
        first_line[j] = line[j];
      }
      first_line[len] = '\0';
      i++;
      continue;
    }
    if (i == 2) {
      second_line_len = len;
      for (int j = 0; j < len; j++) {
        second_line[j] = line[j];
      }
      second_line[len] = '\0';
      i++;
      continue;
    }

    if (i == 3) {
      third_line_len = len;
      for (int j = 0; j < len; j++) {
        third_line[j] = line[j];
      }
      third_line[len] = '\0';

      suma += priority2(first_line, second_line, third_line, first_line_len,
                        second_line_len, third_line_len);
      i = 1;

      continue;
    }
  }

  fclose(file);

  return suma;
}

int main() {
  printf("Part one: %d\n", part_one("dane.txt"));
  printf("Part two: %d\n", part_two("dane.txt"));
  return 0;
}
