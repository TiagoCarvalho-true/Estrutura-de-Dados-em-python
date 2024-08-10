from collections import deque

class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

def inserir (raiz, valor):
        if raiz is None:
            return No(valor)
        else:
            if valor < raiz.valor:
              raiz.esquerda = inserir(raiz.esquerda,valor)
            else:
                raiz.direita= inserir(raiz.direita,valor)

        return raiz
    
def percorrer_em_ordem(raiz):
        if raiz:
            percorrer_em_ordem(raiz.esquerda)
            print(raiz.valor,end='')
            percorrer_em_ordem(raiz.direita)

def percorrer_em_largura(raiz):
        if raiz is None:
            return
        fila = deque()
        fila.append(raiz)
        while fila:
            no =  fila.popleft()
            print(no.valor,end='')
            if no.esquerda:
                fila.append(no.esquerda)
            if no.direita:
                fila.append(no.direita)
            
def percorrer_em_profundidade(raiz):
        if raiz is None:
            return
        pilha = []
        pilha.append(raiz)
        while pilha:
            no = pilha.pop()
            print(no.valor,end='')
            if no.direita:
                 pilha.append(no.direita)
            if no.esquerda:
                 pilha.append(no.esquerda)

    
if __name__== "_main_":
     raiz= None
     valores = [10,5,15,3,7,12,18]
     for valor in valores:
          raiz = inserir(raiz,valor)
    
     print("percorrendo em ordem: ")
     percorrer_em_ordem(raiz)
     print("percorrendo em largura: ")
     percorrer_em_largura(raiz)
     print("percorrendo em profundidade: ")
     percorrer_em_profundidade(raiz)