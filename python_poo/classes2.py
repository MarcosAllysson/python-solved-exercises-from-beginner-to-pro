"""
Cria uma classe Carro com no mínimo 3 propriedades (atributos) e 3 métodos
"""

class Carro:
    # construtor e atributos da classe
    def __init__(self, marca, valor, velocidade_maxima):
        self.marca = marca
        self.valor = float(valor)
        self.velocidade_maxima = int(velocidade_maxima)

    # métodos get
    def getMarca(self):
        return self.marca

    def getValor(self):
        return self.valor

    def getVelocidadeMaxima(self):
        return self.velocidade_maxima


    # métodos set
    def setMarca(self, marca):
        self.marca = marca

    def setValor(self, valor):
        self.valor = float(valor)

    def setVelocidadeMaxima(self, velocidade):
        self.velocidade_maxima = int(velocidade)


    # método de informação geral
    def infoGeral(self):
        print('\033[1;36mINFORMAÇÕES GERAIS SOBRE O CARRO:\033[m ')
        print(f'Marca: {self.getMarca()} \nValor: US$ {self.getValor()} \nVelocidade Máxima: {self.getVelocidadeMaxima()}km/h')

    
carro = Carro('Bugatti', 1000000, 340)
carro.setMarca('Rolls Roice')
carro.setValor(350000)
carro.setVelocidadeMaxima(280)
carro.infoGeral()
