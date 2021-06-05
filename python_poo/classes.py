# definindo classe
class Sample(object):
    # classe não faz nada
    pass

# pra criar um objeto do tipo Sample:
objeto = Sample()
#print(type(objeto)) # um objeto do tipo sample


# DEFININDO ATRIBUTOS E MÉTODOS
class Dog(object):
    # Atributos da classe
    def __init__(self, raca, nome):
        self.raca = raca
        self.nome = nome

    # Métodos da classe
    def latir(self):
        print('Au Au')


sam = Dog('Pit bull', 'Sam')
print(f'Raça: {sam.raca}, nome: {sam.nome}. ')

frank = Dog('Huskie', 'Frank')
print(f'Raça: {frank.raca}, nome: {frank.nome}.')

print('Todo cachorro faz:')
sam.latir()
# print(type(sam))