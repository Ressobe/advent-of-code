#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 256


int *get_range(char buffer[], int size) {
    char line[size];
    strcpy(line, buffer);

    int *range = (int *)malloc(sizeof(int) * 2);

    char *numbers = strtok(line, "-");

    int number1 = atoi(numbers);
    numbers = strtok(NULL, "-");
    int number2 = atoi(numbers);
      
    range[0] = number1;
    range[1] = number2;

    return range;
}


char *get_string(char line[], int size) {
  char buffer[size];
  strcpy(buffer, line);

  char *portion = strtok(buffer, " ");
  portion = strtok(NULL, " ");
  portion = strtok(NULL, " ");

  int len = strlen(portion);

  char *string = (char *)malloc(sizeof(char) * len);

  for (int i = 0; i < len - 1; i++) {
    string[i] = portion[i];
  }
  string[len - 1] = '\0';

  return string;
}

int check_password_valid(char *string, char c, int low_range, int high_range) {
  int i = 0;
  int amount = 0;
  while(string[i] != '\0') {
      if(string[i] == c) {
        amount++;
    }
    i++;
  }
  if ((amount >= low_range) && (amount <= high_range)) {
    return 1;
  }
  else {
    return 0;
  }
}
int check_password_valid_v2(char *string, char c, int first_index, int second_index) {
  if (string[first_index - 1] == c && string[second_index - 1] != c) {
    return 1;
  }

  if (string[first_index - 1] != c && string[second_index - 1] == c) {
    return 1;
  }

  return 0;
}


int main() {
  FILE *input = fopen("input.txt", "r");

  if (input == NULL) {
    printf("Błąd otwarcia pliku");
    return 1;
  }
  

  char buffer[MAX_SIZE];
  int valid_passwords = 0;

  while (fgets(buffer, MAX_SIZE, input) != NULL) {
      int len = strlen(buffer);

      int *range = get_range(buffer, len);
      char *string = get_string(buffer, len);

      char *portion = strtok(buffer, " ");
      portion = strtok(NULL, " ");
      char c = portion[0];

      if (check_password_valid_v2(string, c, range[0], range[1])) {
        valid_passwords++;    
      }
      free(range);
      free(string);
  }

  printf("%d", valid_passwords);

  fclose(input);
  return 0;
}
