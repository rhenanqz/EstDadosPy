## Classe Progression que cria todo o conjunto de numeros naturais:0,1,2...
# Para posterior criação das subclasses ArithmeticProgression,
# GeometricProgression e FibonacciProgression

class Progression:
    def __init__(self, inicio):
        self._valor = inicio #Função

    #Calcula o proximo elemento da sequencia
    #Adiciona 1 a cada valor
    def _avancar(self):
        self._valor += 1

    #Retorna o proximo elemento
    #Toda classe com iterador tem essa função que retorna o proximo da funcao
    def __next__(self):
        if self._valor is None:
            raise StopIteration() #fim
        else:
            resposta = self._valor
            self._avancar() #atualiza o valor corrente
            return resposta

    #e também tem que conter o método __iter__ indicando que é um iterador
    def __iter__(self):
        return self #Por convenção retorna ele msm

    #Imprime os n primeiros elementos da sequência
    def gera_sequencia(self, n):
        L = []
        for j in range(n):
            L.append(next(self))
        return L

if __name__ == '__main__':
    sequencia = Progression(0)
    print(sequencia.gera_sequencia(20))
