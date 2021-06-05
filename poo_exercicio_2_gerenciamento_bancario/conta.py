from cliente import Cliente


class Conta(Cliente):
    def __init__(self, nome, cpf, saldo, limite):
        Cliente.__init__(self, nome, cpf)
        self.saldo = saldo
        self.limite = limite

    # Métodos GET's
    def getLimite(self):
        return self.limite

    # Métodos SET's
    def setSaldo(self, novo_saldo):
        self.saldo = novo_saldo
        print('Saldo alterado!')

    def setLimite(self, limite):
        self.limite = limite
        print('Limite alterado!')

    # Método sacar, depositar e consultar saldo.
    def sacar(self, valor):
        if valor <= self.saldo and valor > 0:
            self.saldo -= valor
            print(f'Valor sacado! Novo saldo: {self.getSaldo()}')
        else:
            print('Saque não alterizado!')

    # Método depositar e consultar saldo.
    def depositar(self, valor_deposito):
        if valor_deposito > 1:
            self.saldo += valor_deposito
            print(f'Valor depositado! Novo saldo: {self.getSaldo()}')
        else:
            print('Deposite pelo menos um valor superior a R$ 1,00')

    # Método consultar saldo.
    def getSaldo(self):
        return self.saldo

    def __str__(self):
        return f'Cliente: {Cliente.__str__(self)}' \
               f'\nSaldo: R$ {self.getSaldo()}' \
               f'\nLimite: R$ {self.getLimite()}.'
