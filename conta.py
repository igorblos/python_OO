class ContaCorrente:

    def __init__(self, numero, titular, saldo, limte):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limte

    def exibir_extrato(self):
        print("Extrado do titulaar {0}:{1}".format(self.titular ,self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        self.exibir_extrato()

    def sacar(self, valor):
        self.saldo -= valor
        self.exibir_extrato()