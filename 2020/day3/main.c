#include <stdio.h>
#include <string.h>


int main() {
  FILE *input = fopen("input.txt", "r");

  char buffer[256];

  int i = 0;
  int trees = 0;
  while(fgets(buffer, 256, input)) {
      int len = strlen(buffer);

      if (i >= len) {
        i = i - len;
      }

      printf("%c \n", buffer[i]);
      if (buffer[i] == '#') {
        trees++;
      }
      i += 3;
  }
  printf("%d", trees);

  fclose(input);
  return 0;
}


