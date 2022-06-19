class CreditCard:
    #Construtor (usado para instanciar objetos)
    def __init__(self, cliente, banco, conta, limite):
        self._cliente = cliente
        self._banco = banco
        self._conta = conta
        self._limite = limite
        self._fatura = 0 #Valor da fatura se inicia com 0
        print('Cartao criado com sucesso')

    def imprime_dados(self):
        print('Cliente: %s' % self._cliente)
        print('Banco: %s' % self._banco)
        print('Conta: %s' % self._conta)
        print('Limite: %s' % self._limite)
        print()

    def get_cliente(self):
        return self._cliente

    def get_banco(self):
        return self._banco

    def get_conta(self):
        return self._conta

    def get_limite(self):
        return self._limite

    def get_fatura(self):
        return self._fatura

    #Função que realiza a compra e lança o Valor
    def compra(self, preco):
        if preco + self._fatura > self._limite:
            print("Limite insuficiente")
        else:
            self._fatura += preco
            print("Compra de R$ %.2f realizada" % preco)
            return True

    def pagamento(self,valor):
        if valor <= self._fatura:
            self._fatura -= valor
            print("Pagamento de R$ %.2f reais da fatura" % valor)

if __name__ == '__main__':
    cartao = CreditCard('Alexandre', 'BB', '11432-5', 1000)
    cartao.imprime_dados()
    print(cartao.get_fatura())
    cartao.compra(250)
    cartao.compra(100)
    cartao.compra(200)
    print(cartao.get_fatura())
    cartao.pagamento(500)
    print(cartao.get_fatura())
