class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def getNome(self):
        return self.nome

    def getCpf(self):
        return self.cpf

    def setNome(self, nome):
        self.nome = nome
        print('Nome alterado!')

    def setCpf(self, cpf):
        self.cpf = cpf
        print('CPF alterado!')

    def __str__(self):
        return f'{self.getNome()}.\nCPF: {self.getCpf()}.'
