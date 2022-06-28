from Pilha import Stack

#Check Parentesis
def verifica_expressao_simples(expressao):
    s = Stack()
    balanceado = True
    for i in range(len(expressao)):
        if expressao[i] == '(':
            s.push(expressao[i])
        elif expressao[i] == ')':
            if s.is_empty():
                balanceado = False
                break
            else:
                s.pop()
    if balanceado and s.is_empty():
        return True
    else:
        return False

def verifica_expressao_composta(expressao):
    # Cria pilha vazia
    s = Stack()
    balanceado = True
    indice = 0 # primeira posição na expressão
    n = len(expressao) # tamanho da expressão (qtde de caracteres)
    # Enquanto não chegar no final e estiver balanceado
    while indice < n and balanceado:
        # Obtém o símbolo atual
        simbolo = expressao[indice]
        # Se símbolo é um dos abre parêntesis, empilha
        if simbolo in '([{':
            s.push(simbolo)
        # Se for algum fechamento, o abre tem que estar na pilha
        # Se não estiver na pilha, não está balanceado
        elif simbolo in ')]}':
            if s.is_empty():
                balanceado = False
            else: # Se abre está na pilha, verifica se são iguais
                abre = s.pop()
        # Se o abre e o fecha não são iguais, está desbalanceado
                if (simbolo == '}' and abre != '{') or \
                    (simbolo == ']' and abre != '[') or \
                    (simbolo == ')' and abre != '('):
                    balanceado = False
        indice += 1
    if balanceado and s.is_empty():
        return True
    else:
        return False

if __name__ == '__main__':
    print('Expressões simples')
    print(verifica_expressao_simples('((1 + 2) * (3 + 4)) - (5 + 6)'))
    print()
    print(verifica_expressao_simples('((1 + 2) * (3 + 4))))'))
    print()
    print(verifica_expressao_simples('(((((1 + 2) * (3 + 4))'))
    print()

    print('Expressões compostas')
    print(verifica_expressao_composta('{ [ (1 + 2) + (3 + 4) ] * 2 }'))
    print()
    print(verifica_expressao_composta('{ [ (1 + 2} + [3 + 4} ) * 2 )'))
