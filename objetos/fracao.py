class Fracao:
    #Construtor
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

    #Imprime a fracao na tela
    def show(self):
        print("%s/%s" % (self.num,self.den))

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    #Multiplica as fracoes
    def __mul__(self, other):
        num_mul = self.num * other.num
        den_mul = self.den * other.den
        return Fracao(num_mul, den_mul)

    #Adiciona fracoes
    def __add__(self, other):
        num_add = self.num * other.den + self.den * other.num
        den_add = self.den * other.den
        return Fracao(num_add, den_add)

    #Simplifica fracoes
    def simplifica(self):
        m = self.num
        n = self.den
        while n > 0:
            m, n = n, m % n
        mdc = m
        return Fracao(self.num//mdc, self.den//mdc)

    #Verifica se duas fracoe sao iguais
    def __eq__(self,other):
        f1 = self.simplifica()
        f2 = other.simplifica()
        return ((f1.num == f2.num) and (f1.den==f2.den))

    def __sub__(self, other):
        neg_other_num = -other.num
        neg_other_den = other.den
        sub = self + (Fracao(neg_other_num,neg_other_den))
        return Fracao(sub.num, sub.den)

    def inverter(self):
        return Fracao(self.den,self.num)
