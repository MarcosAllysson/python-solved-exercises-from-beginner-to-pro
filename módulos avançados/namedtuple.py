"""
Para casos de uso simples, isso geralmente é suficiente. Por outro lado, lembrar qual índice deve ser
usado para cada valor pode levar a erros, especialmente se a tupla tiver muitos campos e for construída
longe de onde ela é usada. Um namedtuple atribui nomes, bem como o índice numérico, a cada membro.

Cada tipo de namedtuple é representado por sua própria classe, criado usando a função de fábrica namedtuple().
Os argumentos são o nome da nova classe e uma string contendo os nomes dos elementos.

Você basicamente deve pensar o namedtuple como uma maneira muito rápida de criar um novo tipo de
objeto / classe com alguns campos de atributos.
"""
from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2, breed='Lab', name='Sammy')
frank = Dog(age=2, breed='Shepard', name="Frankie")

print(sam)
print(sam.age, sam.breed, sam.name)

print()
print(frank)
