import numpy as np

class Integration:
    def __init__(self, f):
        self.f = f #função a ser imputada

    #Método de Simpson
    def Simpson(self, a, b, n):
        h = (b-a)/n #espaço entre os intervalos
        soma_pares, soma_impares = 0,0
        #Soma dos pares
        for i in range(2, n, 2):
            k = a + i*h
            soma_pares += self.f(k)
        #Soma dos impares
        for i in range(1, n, 2):
            k = a + i*h
            soma_impares += self.f(k)

        area = (h/3)*(self.f(a) + 4*soma_impares + 2*soma_pares + self.f(b))
        return area

    #Metodo de Simpson 3/8
    def Simpson_3_8(self, a, b, n):
        h = (b-a)/n
        soma_mult_3, soma_restante =0,0
        for i in range(1, n):
            k = a + i*h
            if i%3 == 0:
                soma_mult_3 += self.f(k)
            else:
                soma_restante += self.f(k)
        area = (3*h/8)*(self.f(a) + 2*soma_mult_3 + 3*soma_restante + self.f(b))
        return area

    def Simpson_ext(self, a, b, n):
        area = None
        h = (b-a)/n

        if n <= 8:
            print('Numero insuficiente de pontos')
        else:
            soma_meio = 0
            for i in range(4,n-3):
                k = a + i*h
                soma_meio += self.f(k)
            soma = (17*(self.f(a) + self.f(b)) + \
                    59*(self.f(a+h) + self.f(a+(n-1)*h)) + \
                    43*(self.f(a+2*h) + self.f(a+(n-2)*h)) + \
                    49*(self.f(a+3*h) + self.f(a+(n-3)*h)) +\
                    48*soma_meio)
            area = soma*(h/48)
        return area

if __name__ == '__main__':
    f = lambda x: np.sqrt(1+x**3)
    g = lambda x: 1/np.sqrt((1 + x**4))
    # Densidade Normal(0, 1)
    p = lambda x: (1/(2*np.pi)**0.5)*np.exp(-0.5*x**2)

    # Função f
    metodo = Integration(f)
    print("Função np.sqrt(1+x**3)")
    print("Simpson: ", metodo.Simpson(1,4,20))
    print("Simpson 3/8: ", metodo.Simpson_3_8(1,4,21))
    print('Simpson Ext: ', metodo.Simpson_ext(1,4,21))
    print()

    # Função g
    metodo = Integration(g)
    print("Função 1/np.sqrt((1 + x**4))")
    print('Simpson: ', metodo.Simpson(0, 2, 20))
    print('Simpson 3/8: ', metodo.Simpson_3_8(0, 2, 21))
    print('Simpson Ext: ', metodo.Simpson_ext(0, 2, 6))
    print('Simpson Ext: ', metodo.Simpson_ext(0, 2, 41))
    print()

    # Função p
    metodo = Integration(p)
    print("Função (1/(2*np.pi)**0.5)*np.exp(-0.5*x**2)")
    print('Simpson: ', metodo.Simpson(0, 3, 20))
    print('Simpson 3/8: ', metodo.Simpson_3_8(0, 3, 21))
    print('Simpson Ext: ', metodo.Simpson_ext(0, 3, 80))
    print()
