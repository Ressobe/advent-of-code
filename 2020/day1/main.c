#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_SIZE 256

void print_array(int *array, int length) {

  for (int i = 0 ; i < length; i++) {
    printf("%d\n", array[i]);
  }

}

int sum(int *array, int length) {
  for (int i = 0; i < length - 1; i++) {
    for (int j = i + 1; j < length; j++) {
      if (array[i] + array[j] == 2020) {
        return array[i] * array[j];
      }
    }
  }
  return -1;
}

int sum2(int *array, int length) {
  for (int i = 0; i < length - 2; i++) {
      if(array[i] > 2020) continue;
      for (int j = i + 1; j < length - 1; j++) {
        if(array[j] > 2020) continue;
        for(int k = j + 1; k < length; k++) {
          if(array[i] + array[j] + array[k] == 2020) {
            return array[i] * array[j] * array[k];
        }
      }
    }
  }
  return 0;
}

int main() {

  FILE *input = fopen("input.txt", "r");

  if (input == NULL) {
    printf("Błąd otwarcia pliku");
    return -1;
  }
   
  int ile_liczb = 0;
  int liczba;
  while(fscanf(input, "%d", &liczba) != EOF) {
    ile_liczb++; 
  }

  int *array = (int*)malloc(sizeof(int) * ile_liczb);
  
  fseek(input, 0, SEEK_SET);
  int i = 0;

  while((fscanf(input, "%d", &liczba) != EOF ) && i < ile_liczb) {
    array[i] = liczba;
    i++;
  }

  printf("%d\n", sum2(array, ile_liczb));

  free(array);
  fclose(input);
  return 0;
}

