from Progression import Progression
class FibonacciProgression(Progression):
# Construtor (usado para instanciar novos objetos)
    def __init__(self, primeiro=0, segundo=1):
        super().__init__(segundo)
        self._previo = primeiro

    def _avancar(self):
        self._previo,self._valor=self._valor,self._previo+self._valor
        
if __name__ == '__main__':
# Instancia objeto
    n = int(input('Entre com o número de termos: '))
    Fib = FibonacciProgression()
    print(Fib.gera_sequencia(n))
