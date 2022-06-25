'''
Crie uma árvore para cada lista abaixo, adicione um valor nela e remova outro, mas,
em pelo menos uma das árvores, a remoção deve ser de um nó com dois filhos.
Lista1 = 45,20,30,60,81,97,100,7,8,4
Lista2 = 15,6,18,3,7,16,20,4
'''
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
    
    def getChave(self):
        return self.__chave

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
        if self.__chave < valor: # direita
            if self.__direita is None:
                print(f'Valor {valor} não foi encontrado.')
            else:
                self.__direita = self.__direita.remove(valor)

        elif self.__chave > valor: # esquerda
            if self.__esquerda is None:
                print(f'Valor {valor} não foi encontrado.')
                return
            else:
                self.__esquerda = self.__esquerda.remove(valor)
                
        else: # remover
            print(f'Valor {self.__chave} encontrado.')
            if self.__direita is None and self.__esquerda is None:
                # não tem nodos filho
                print(f'Valor {valor} removido com sucesso.')
                return None

            if self.__direita is None:
                # tem só um nodo filho à esquerda
                print(f'Valor {valor} removido com sucesso.')
                return self.__esquerda

            if self.__esquerda is None:
                # tem só um nodo filho à direita
                print(f'Valor {valor} removido com sucesso.')
                return self.__direita
            
            # tem dois nodos filho
            aux = self.__direita
            esquerda = self.getEsquerda()
            self.__chave = self.__direita.getChave()
            self.__esquerda = self.__direita.getEsquerda()
            self.__direita = self.__direita.getDireita()
            self.insere(esquerda)
            print(f'Valor {valor} removido com sucesso.')
            del aux
        return self
                        
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

print('Árvore 1:')
arvore1.printArvore()
num = 50
print(f'Adicionando o valor {num} à árvore 1 e imprimindo novamente:')
arvore1.insere(NodoArvore(num))
arvore1.printArvore()

num = 60
print(f'Removendo elemento {num} da árvore 1:')
arvore1.remove(num)
print('Árvore 1 atualizada:')
arvore1.printArvore()

# Árvore 2
lista2 = [15,6,18,3,7,16,20,4]
arvore2 = NodoArvore(lista2[0])
for chave in lista2[1:]:
    arvore2.insere(NodoArvore(chave))

print('Árvore 2:')
arvore2.printArvore()
num = 2
print(f'Adicionando o valor {num} à árvore 2 e imprimindo novamente:')
arvore2.insere(NodoArvore(num))
arvore2.printArvore()

num = 18
print(f'Removendo elemento {num} da árvore 2:')
arvore2.remove(num)
print('Árvore 2 atualizada:')
arvore2.printArvore()