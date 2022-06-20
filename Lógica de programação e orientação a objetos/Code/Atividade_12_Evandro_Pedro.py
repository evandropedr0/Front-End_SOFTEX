class NodoArvore:   
    def __init__(self, chave=None):
        self.__chave = chave
        self.__esquerda = None
        self.__direita = None
        
    def __repr__(self):
        return '%s <- %s -> %s' % (self.__esquerda and self.__esquerda.__chave,
                                    self.__chave,
                                    self.__direita and self.__direita.__chave)

    def em_ordem(self):
        if not self:
            return

        # Visita filho da esquerda.
        em_ordem(self.__esquerda)

        # Visita nodo corrente.
        print(self.__chave),

        # Visita filho da direita.
        em_ordem(self.__direita)

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
                self.insere(self.__direita, nodo)

        # Nodo deve ser inserido na subárvore esquerda.
        else:
            if self.__esquerda is None:
                self.__esquerda = nodo
            else:
                self.insere(self.__esquerda, nodo)

raiz = NodoArvore(3)
raiz.insere(NodoArvore(1))
raiz.insere(NodoArvore(5))
raiz.insere(NodoArvore(2))
# raiz.insere(NodoArvore(7))
# raiz.insere(NodoArvore(10))
# raiz.insere(NodoArvore(0))
print("Árvore: ")
print(raiz)