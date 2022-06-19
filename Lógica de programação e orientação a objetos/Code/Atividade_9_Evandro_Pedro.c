// Crie um vetor com ponteiros utilizando alocação dinâmica na linguagem C, que:

// - use a função realloc;
// - use a função sizeof;
// - que tenha tamanho 22 de vetor;
// - depois libere o bloco utilizando a função free.

#include <stdio.h>
#include <stdlib.h>

int main(){
    int * ponteiro;
    int * aux;

    ponteiro = (int *) malloc(10 * sizeof(int));
    printf("Tamanho do ponteiro apos malloc: %d\n", sizeof(ponteiro));

    printf("Conteudo do vetor (malloc):\n");
    aux = ponteiro;
    for (int i = 0; i < 10; i++){
        printf("%d\n",*aux);
        aux++;
    }

    free(ponteiro);
    
    ponteiro = (int *) calloc(10, sizeof(int));
    printf("Tamanho do ponteiro apos calloc: %d\n", sizeof(ponteiro));

    printf("Conteudo do vetor (calloc):\n");
    aux = ponteiro;
    for (int i = 0; i < 10; i++){
        printf("%d\n",*aux);
        aux++;
    }

    ponteiro = (int *) realloc(ponteiro, 22 * sizeof(int));
    printf("Tamanho do ponteiro apos realloc: %d\n", sizeof(ponteiro));

    printf("Conteudo do vetor (realloc):\n");
    aux = ponteiro;
    for (int i = 0; i < 22; i++){
        printf("%d\n",*aux);
        aux++;
    }

    free(ponteiro);
    return 0;
}