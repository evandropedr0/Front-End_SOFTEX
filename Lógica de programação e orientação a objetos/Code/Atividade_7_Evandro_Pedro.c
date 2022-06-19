#include<stdio.h>

void bubble_sort (int vetor[], int n) {
    int k, j, aux;

    for (k = 1; k < n; k++) {
        printf("\n[%d] ", k);

        for (j = 0; j < n - k; j++) {
            printf("%d, ", j);

            if (vetor[j] > vetor[j + 1]) {
                aux          = vetor[j];
                vetor[j]     = vetor[j + 1];
                vetor[j + 1] = aux;
            }
        }
    }
    printf("\n");
}

void printVetor(int vetor[], int n){
    printf("[ ");
    for(int i = 0; i < n-1; i++){
        printf("%d, ", vetor[i]);
    }
    printf("%d ",vetor[n-1]);
    printf("]\n");
}

int main(){

    int vetor[10] = {10,4,2,1,5,6,8,7,9,3};
    size_t tamanhoVetor = sizeof(vetor)/sizeof(vetor[0]);
    printf("\nVetor original:\n");
    printVetor(vetor,tamanhoVetor);
    bubble_sort(vetor,tamanhoVetor);
    printf("\nVetor ordenado:\n");
    printVetor(vetor, tamanhoVetor);
    printf("\n");

    return 0;
}