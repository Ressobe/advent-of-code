#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void print_array(int *array, int length) {
  printf("[");
  for (int i = 0; i < length; i++) {
    if (i == length - 1) {
      printf("%d", array[i]);
    } else {
      printf("%d, ", array[i]);
    }
  }
  printf("]\n");
}

void bubble_sort(int *numbers, int length) {
  for (int i = 0; i < length; i++) {
    for (int j = 0; j < length - 1 - i; j++) {
      if (numbers[j + 1] < numbers[j]) {
        int temp = numbers[j];
        numbers[j] = numbers[j + 1];
        numbers[j + 1] = temp;
      }
    }
  }
}

int part_one(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return 1;

  char line[100];
  int max_suma = 0;
  int suma = 0;
  while (fgets(line, sizeof(line), file)) {
    int num = atoi(line);
    if (num) {
      suma += num;
    } else {
      if (suma > max_suma) {
        max_suma = suma;
      }
      suma = 0;
    }
  }

  fclose(file);

  return max_suma;
}

int part_two(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return 1;

  char line[100];
  int count_numbers = 1;
  while (fgets(line, sizeof(line), file)) {
    int num = atoi(line);
    if (!num) {
      count_numbers++;
    }
  }

  int sums[count_numbers];
  int i = 0;
  int suma = 0;
  fseek(file, 0, SEEK_SET);

  while (fgets(line, sizeof(line), file)) {
    int num = atoi(line);
    if (num) {
      suma += num;
    } else {
      sums[i] = suma;
      suma = 0;
      i++;
    }
  }
  if (suma != 0)
    sums[i] = suma;

  bubble_sort(sums, count_numbers);

  fclose(file);
  return sums[count_numbers - 1] + sums[count_numbers - 2] +
         sums[count_numbers - 3];
}

int main() {
  printf("Part one: %d\n", part_one("dane.txt"));
  printf("Part two: %d", part_two("dane.txt"));
  return 0;
}

// Trying something :)
int count_lines_in_file(FILE *file) {
  int linesCounter = 0;
  char c;
  while ((c = fgetc(file)) != EOF) {
    if (c == '\n') {
      linesCounter++;
    }
  }
  return linesCounter;
}

char *read_from_file(char *filename) {
  FILE *file;

  file = fopen(filename, "r");
  if (file == NULL)
    return NULL;

  fseek(file, 0, SEEK_END);
  int length = ftell(file);
  char c;
  fseek(file, 0, SEEK_SET);

  char *string = (char *)malloc(sizeof(char) * (length + 1));

  int lines = count_lines_in_file(file);
  int *pArray[lines];
  // printf("%d", length);

  char buffer[1024];
  int cn;
  while (fgets(buffer, 1024, file)) {
    cn = strnlen(buffer, 1024);
    printf("%d", cn);
  }
  //
  //
  // int i = 0;
  // while ((c = fgetc(file)) != EOF) {
  //   string[i] = c;
  //   i++;
  // }
  // string[i] = '\0';

  fclose(file);

  return string;
}
