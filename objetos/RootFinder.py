import numpy as np

class RootFinder:
    def __init__(self, f, d):
        self.f = f
        self.df = df    #Derivada da função

    #Metodo de Newton
    #x0: chute inicial
    #epson: tolerancia
    def Newton(self, x0, epson):
        x = x0
        novo_x = np.random.random()
        erro = abs(x-novo_x)
        while erro >= epson:
            novo_x = x - f(x)/df(x)
            erro = abs(x-novo_x)
            print('x:%.10f ******** Erro: %.10f' %(novo_x, erro))
            x = novo_x
        return x

    #Método da Secante
    #x0, x1: chutes iniciais
    #epson: tolerancia
    def Secante(self, x0, x1, epson):
        erro = abs(x0 - x1)
        while erro >= epson:
            novo_x = x1 - f(x1)*(x1-x0)/(f(x1) - f(x0))
            erro = abs(x1 - novo_x)
            print('x:%.10f ******** Erro: %.10f' %(novo_x, erro))
            x0, x1 = x1, novo_x
        return novo_x

if __name__ ==  '__main__':
    f = lambda x: x**3 + x - 1 #Função cuja raiz sera encontrada
    df = lambda x: 3*x**2 + 1
    metodo = RootFinder(f,df)
    metodo.Newton(0, 10**(-8))
    print()
    metodo.Secante(0,1,10**(-8))
