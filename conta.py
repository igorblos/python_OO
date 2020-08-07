class ContaCorrente:

    def __init__(self, numero, titular, saldo, limte):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limte

    def exibir_extrato(self):
        print("Extrado do titulaar {0}:{1}".format(self.__titular, self.__saldo))

    def depositar(self, valor, exibir_extrato=False):
        self.__saldo += valor
        if(exibir_extrato):
            self.exibir_extrato()

    def __pode_sacar(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= (valor_disponivel)

    def sacar(self, valor, exibir_extrato=False):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
            if(exibir_extrato):
                self.exibir_extrato()
        else:
            print("O valor {0} passou o limite".format(valor))

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
