from Progression import Progression

#Herança a partit da superclasse Progression
class GeometricProgression(Progression):
    def __init__(self, inicio, razao):
        super().__init__(inicio)
        self._razao = razao

    def _avancar(self):
        self._valor *= self._razao

if __name__ == '__main__':
    a0 = int(input('Entre com o valor de a0:'))
    razao = float(input('Entre com o valor da razão: '))
    n = int(input('Enter com o número de termos: '))
    PG = GeometricProgression(a0, razao)
    print(PG.gera_sequencia(n))
    
