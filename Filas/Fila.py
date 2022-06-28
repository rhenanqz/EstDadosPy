class Queue:
    #Inicializa a fila
    def __init__(self):
        self.itens = []
    #insere um elemento
    def enqueue(self, item):
        self.itens.insert(0,item)
    #Remove um elemento
    def dequeue(self):
        return self.itens.pop()
    #Checa se está vazia
    def is_empty(self):
        return self.itens == []
    #Retorna o tamanho
    def size(self):
        return len(self.itens)
    #Imprime a fila na tela
    def print_queue(self):
        print(self.itens)

if __name__ == '__main__':
    Q = Queue()
    Q.print_queue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.print_queue()
    Q.dequeue()
    Q.dequeue()
    Q.print_queue()
    Q.enqueue(7)
    Q.enqueue(8)
    Q.enqueue(9)
    Q.print_queue()
    print(Q.is_empty())
