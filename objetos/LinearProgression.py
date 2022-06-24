from Progression import Progression
class LinearProgression(Progression):
    def __init__(self, t0, t1, a, b):
        super().__init__(t1)
        self._t0 = t0
        self._a = a
        self._b = b
    def _avancar(self):
        self._valor, self._t0 = self._a*self._valor + b*self._t0, self._valor

if __name__ == '__main__':
# Instancia objeto
    t0 = int(input('Entre com t0: '))
    t1 = int(input('Entre com t1: '))
    a = int(input('Entre com a: '))
    b = int(input('Entre com b: '))
    n = int(input('Entre com o número de termos: '))
    Lin = LinearProgression(t0,t1,a,b)
    print(Lin.gera_sequencia(n))


#a = 1, b = 2
#0        3
#1        4
#2        1*4+2*3 = 10    a*t1 +b*t0
#3        1*10+2*4 = 18
