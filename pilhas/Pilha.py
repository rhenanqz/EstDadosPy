class Stack:
    #inicia uma lista vazia
    def __init__(self):
        self.itens = []

    #Verifica se a lista está vazia
    def is_empty(self):
        return self.itens == []

    #Insere um elemento no topo
    def push(self, elemento):
        self.itens.append(elemento)

    #Obtem um elemento do topo
    def peek(self):
        return self.itens[-1]

    #Retira um elemento do topo
    def pop(self):
        return self.itens.pop()

    #Tamanho de uma lista
    def size(self):
        return len(self.itens)

    #Mostra a lista
    def print_stack(self):
        print(self.itens)

if __name__ == '__main__':
    S = Stack()
    S.print_stack()
    S.push(1)
    S.push(2)
    S.push(3)
    S.print_stack()
    S.pop()
    S.pop()
    S.print_stack()
    S.push(7)
    S.push(8)
    S.push(9)
    S.print_stack()
    print(S.is_empty())
