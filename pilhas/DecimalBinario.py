from Pilha import Stack
def decimal_binario(numero):
    s = Stack()
    while numero > 0:
        resto = numero % 2
        s.push(resto)
        numero = numero // 2
    binario = ''
    while not s.is_empty():
        binario = binario + str(s.pop())
    return binario

if __name__ == '__main__':
    n = int(input("Entre com o número inteiro:"))
    print(decimal_binario(n))
