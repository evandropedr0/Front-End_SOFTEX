# Crie uma árvore para cada lista abaixo, adicione um valor nela e remova outro, mas,
# em pelo menos uma das árvores, a remoção deve ser de um nó com dois filhos.
# Lista1 = 45,20,30,60,81,97,100,7,8,4
# Lista2 = 15,6,18,3,7,16,20,4

class NodoArvore:   
    def __init__(self, chave=None):
        self.__chave = chave
        self.__esquerda = None
        self.__direita = None
        
    def __repr__(self):
        return '%s <- %s -> %s' % (self.__esquerda and self.__esquerda.__chave,
                                    self.__chave,
                                    self.__direita and self.__direita.__chave)

    def getEsquerda(self):
        return self.__esquerda

    def getDireita(self):
        return self.__direita

    def em_ordem(self):
        if self is None:
            return
        else:
            if self.__esquerda is not None:
                # Visita filho da esquerda.
                self.__esquerda.em_ordem()

            # Visita nodo corrente.
            print(self.__chave),

            if self.__direita is not None:
                # Visita filho da direita.
                self.__direita.em_ordem()

    def insere(self, nodo):
        '''Insere um nodo em uma árvore binária de pesquisa.'''
        # Nodo deve ser inserido na raiz.
        if self is None:
            self = nodo

        # Nodo deve ser inserido na subárvore direita.
        elif self.__chave < nodo.__chave:
            if self.__direita is None:
                self.__direita = nodo
            else:
                self.__direita.insere(nodo)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if self.__esquerda is None:
                self.__esquerda = nodo
            else:
                self.__esquerda.insere(nodo)
                
    def remove(self, valor):
        if self is None:
            print(f'Valor {valor} não foi encontrado.')
            return
        else:
            if self.__chave == valor: # remove
                
                if self.__direita is None and self.__esquerda is None:
                    # não tem nodos folha
                    aux = self
                    self = None
                    del aux
                    print(f'Valor {valor} removido com sucesso.')

                elif self.__direita is None and self.__esquerda is not None:
                    # tem só um nodo folha à esquerda
                    aux = self
                    esquerda = self.__esquerda
                    self.__esquerda = self.__esquerda.getEsquerda()
                    self.__direita = self.__esquerda.getDireita()
                    self = esquerda
                    del aux
                    print(f'Valor {valor} removido com sucesso.')

                elif self.__direita is not None and self.__esquerda is None:
                    # tem só um nodo folha à direita
                    aux = self
                    direita = self.__direita
                    self.__esquerda = self.__direita.getEsquerda()
                    self.__direita = self.__direita.getDireita()
                    self = direita
                    del aux
                    print(f'Valor {valor} removido com sucesso.')
                else:
                    # tem dois nodos folha
                    # aux = self
                    # esquerda = self.__esquerda
                    # direita = self.__direita
                    # self.__esquerda = self.__direita.getEsquerda()
                    # self.__direita = self.__direita.getDireita()
                    # self = direita
                    # self.insere(esquerda)
                    
                    # del aux
                    self = self.__direita
                    print(f'Valor {valor} removido com sucesso.')

            elif self.__chave < valor:
                # direita
                if self.__direita is None:
                    print(f'Valor {valor} não foi encontrado.')
                else:
                    self.__direita.remove(valor)

            else:
                # esquerda
                if self.__esquerda is None:
                    print(f'Valor {valor} não foi encontrado.')
                    return
                else:
                    self.__esquerda.remove(valor)
                        
    def printArvore(self):
        if self is not None:
            print(self)
            if self.__esquerda is not None:
                self.__esquerda.printArvore()
                
            if self.__direita is not None:
                self.__direita.printArvore()
                
        


# Árvore 1
lista1 = [45,20,30,60,81,97,100,7,8,4]
arvore1 = NodoArvore(lista1[0])
for chave in lista1[1:]:
    arvore1.insere(NodoArvore(chave))

arvore1.printArvore()
print('Árvore 1 em ordem crescente: ')
arvore1.em_ordem()
print('Adicionando o valor 50 à árvore 1 e imprimindo novamente em ordem crescente:')
arvore1.insere(NodoArvore(50))
arvore1.em_ordem()

print('Removendo elemento 20 da árvore 1:')
arvore1.remove(20)
print('Árvore 1 atualizada:')
arvore1.printArvore()

# # Árvore 2
# lista2 = [15,6,18,3,7,16,20,4]
# arvore2 = NodoArvore(lista2[0])
# for chave in lista2[1:]:
#     arvore2.insere(NodoArvore(chave))
# print("Primeiros elementos da árvore 2: ", arvore2)
# print('Árvore 2 em ordem crescente: ')
# arvore2.em_ordem()
# print('Adicionando o valor 8 à árvore 2 e imprimindo novamente em ordem crescente:')
# arvore2.insere(NodoArvore(8))
# arvore2.em_ordem()