from Progression import Progression

#Herança a partir da superclasse Progression
class ArithmeticProgression(Progression):
    def __init__(self, inicio, razao):
        super().__init__(inicio)
        self._razao = razao

    #Aplicação do polimorfismo - sobrecarga da função herdada da superclasse
    def _avancar(self):
        self._valor += self._razao

if __name__ == '__main__':
    #Instanciando o objeto
    a0 = int(input('Entre com o valor de a0:'))
    razao = int(input('Entre com o valor da razao:'))
    n = int(input('Entre com o número de termos:'))
    PA = ArithmeticProgression(a0, razao)
    print(PA.gera_sequencia(n))
