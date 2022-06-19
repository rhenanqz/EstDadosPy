from CreditCard import CreditCard
# Essa declaração diz que estamos herdando da superclasse CreditCard
class PredatoryCreditCard(CreditCard):
# Construtor (usado para instanciar novos objetos)
    def __init__(self, cliente, banco, conta, limite, juros):
        super().__init__(cliente, banco, conta, limite)
        self._juros = juros
    #Exemplo de polimorfismo em que um método com mesmo nome tem outra função
    def imprime_dados(self):
        print('Cliente: %s' %self._cliente)
        print('Banco: %s' %self._banco)
        print('Conta: %s' %self._conta)
        print('Limite: %.2f' %self._limite)
        print('Juros/ano: %.2f' %self._juros)
        print()
    # As funções de get são herdadas da superclasse

    # Função que penaliza se vc faz uma compra acima do Limite
    def compra(self, preco):
        sucesso = super().compra(preco)
        if not sucesso:
            self._fatura += 10
            print('Multa por ultrapassar limite: + R$ 10')
        return sucesso

    #Função que aplica juros ao final do mês
    def processa_mes(self):
        if self._fatura > 0:
            juros_mes = (1 + self._juros)**(1/12) # juros no mês
            self._fatura *= juros_mes
            print('Fatura corrigida = %f' %self._fatura)

if __name__ == '__main__':
    cartao = PredatoryCreditCard('Fulano','HSBC','99372-5', 500, 300)
    cartao.imprime_dados()
    print(cartao.get_fatura())
    cartao.compra(250)
    cartao.compra(100)
    print(cartao.get_fatura())
    cartao.processa_mes()
    cartao.get_fatura()
    cartao.compra(500)
    cartao.get_fatura()
    cartao.pagamento(200)
    print(cartao.get_fatura())
