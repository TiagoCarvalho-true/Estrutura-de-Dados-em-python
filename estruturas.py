from collections import deque


def criar_matriz():
    matriz = []
    for i in range (3):
        linha = []
        for j in range(3):
            linha.append(0)
            matriz.append(linha)
    return matriz

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)


class Pilha:
    def __init__(self):
        self.items=[]

    def esta_vazia(self):
        return self.items==[]

    def empilhar(self,item):
        self.items.append(item)

    def desempilhar(self):
        return self.items.pop()
    
    def topo(self):
        return self.items[-1]
    
class Fila:
    def __init__(self):
        self.items = deque()
    
    def esta_vazia(self):
        return len(self.items) == 0
    
    def enfileirar(self,item):
        self.items.append(item)

    def desenfileirar(self):
        return self.items.popleft()

    def frente(self):
        return self.items[0]


if __name__ == "_main_":
    matriz = criar_matriz()
    print("Matriz inicial: ")
    imprimir_matriz(matriz)

    pilha = Pilha()
    pilha.empilhar(1)
    pilha.empilhar(2)
    pilha.empilhar(3)
    print("Topo da pilha: ",pilha.topo())
    pilha.desempilhar()
    print("Topo da pilha apos desempilhar: ",pilha.topo())

    fila = Fila()
    fila.enfileirar(1)
    fila.enfileirar(2)
    fila.enfileirar(3)
    print("frente da fila: ", fila.frente())
    print("Frente da fila apos desenfileirar", fila.frente())

