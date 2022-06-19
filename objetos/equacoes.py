from math import sqrt
from math import isnan
# <%% djsjdj>

class Equacao_Quadratica:
    #Construtor
    def __init__(self, a, b, c):
        self.__a = float(a) #__ define variavel privada
        self.__b = float(b)
        self.__c = float(c)
        self.__delta = float('nan')
        self.__x1 = float('nan')
        self.__x2 = float('nan')

    #obtem o valor de a, b, c, delta
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getDelta(self):
        return self.__delta

    #Seta novos valores pra a,b,c
    def setA(self,a):
        self.__a = float(a)

    def setB(self,b):
        self.__b = float(b)

    def setC(self,c):
        self.__c = float(c)

    #Imprime a string da equacao
    def __str__(self):
        return str(self.__a) + 'x^2 + ' + str(self.__b)+'x + ' + str(self.__c)

    #Verifica se é quadratica
    def eh_quadratica(self):
        if self.__a != 0:
            return True

    #Calcula __delta
    def calcula_delta(self):
        self.__delta = self.__b**2 - 4 * self.__a * self.__c

    #Raiz real
    def raiz_real(self):
        if self.__delta > 0:
            return True

    #Resolve Equacao
    def resolve(self):
        if self.eh_quadratica():
            self.calcula_delta()
            if self.raiz_real():
                self.__x1 = (-self.__b + sqrt(self.__delta)/(2*self.__a))
                self.__x2 = (-self.__b - sqrt(self.__delta)/(2*self.__a))
                return (self.__x1, self.__x2)
            else:
                print('A equacao nao admite raizes reais')
        else:
            print('A equacao nao e de segundo grau (a = 0)')

if __name__ == '__main__':
    equacao = Equacao_Quadratica(1,-5,6)
    print(equacao)
    print(equacao.resolve())
