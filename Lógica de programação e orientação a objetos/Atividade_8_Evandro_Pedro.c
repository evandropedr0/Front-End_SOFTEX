#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void insertionSort(int vector[], size_t tamanho) {
	for (int i = 1; i < tamanho; i++) { 
		
		int j = i;
	
		while (j > 0 && vector[j] < vector[j-1]) {
			int aux = vector[j];
			vector[j] = vector[j - 1];
			vector[j - 1] = aux;
			j -= 1;
		}
	
	}	
}

void printVetor(int vetor[], int n){
    printf("[ ");
    for(int i = 0; i < n-1; i++){
        printf("%d,\t", vetor[i]);
        if ((i+1) % 10 == 0)
            printf("\n  ");
    }
    printf("%d ",vetor[n-1]);
    printf("]\n");
}

int main(){
    size_t tamanhoVetor = 30;
    int vetor[tamanhoVetor];

    srand(time(NULL));

    for (int i = 0; i < tamanhoVetor; i++) { 
        vetor[i] = (rand() % 201) - 100;
        if (vetor[i] % 2 == 0)
            vetor[i] += 1;
    }

    printf("Vetor original:\n");
    printVetor(vetor, tamanhoVetor);

    insertionSort(vetor, tamanhoVetor);

    printf("Vetor ordenado:\n");
    printVetor(vetor, tamanhoVetor);

    return 0;
}