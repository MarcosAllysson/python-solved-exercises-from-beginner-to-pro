class Animal:
    def __init__(self):
        print('Animal criado.')

    def quemSouEu(self):
        print('Isso é um animal.')

    def comer(self):
        print('Comendo...')

# animal1 = Animal()
# animal1.quemSouEu()
# animal1.comer()


# pra herdar outra classe, basta passar o nome dela como parâmetro
class Cachorro(Animal):
    def __init__(self):
        # referenciando construtor da classe herdada.
        Animal.__init__(self)
        print('Cachorro criado.')

    def quemSouEu(self):
        # return super().quemSouEu()
        print('Isso é um cachorro.')

    def latir(self):
        print('Cachorro latindo...')


animal2 = Cachorro()
animal2.quemSouEu()
animal2.latir()
animal2.comer()
