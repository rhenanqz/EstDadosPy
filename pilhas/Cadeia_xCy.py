from Pilha import Stack

def cadeia(expressao):
    s = Stack()
    indice = 0
    if 'C' in expressao:
        x = expressao.split('C')[0]
        y = expressao.split('C')[1]
        for i in range(len(x)):
            s.push(x[i])
        pilha_x = ''
        while not s.is_empty():
            pilha_x = pilha_x + str(s.pop())

        if pilha_x == y:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    n = input('Entre com a expressao: ')
    print(cadeia(n))
