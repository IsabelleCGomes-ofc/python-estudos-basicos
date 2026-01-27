class Conta:
    def __init__(self, titular, numero, saldo):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente :/")

    def depositar(self, valor):
        self.saldo += valor

    def Extrato(self):
        print("Cliente:", self.titular, "|| Saldo atual:", self.saldo)
