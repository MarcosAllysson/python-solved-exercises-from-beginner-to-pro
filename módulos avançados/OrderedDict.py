"""
Um OrderedDict é uma subclasse de dicionário que lembra a ordem em que seu conteúdo é adicionado.
"""

#Um exemplo de um dicionário normal:
from collections import OrderedDict

print('Normal dictionary:')

d = {}

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)


#Um dicionário ordenado:
print('OrderedDict:')

d = OrderedDict()

d['a'] = 'A'
d['b'] = 'B'
d['c'] = 'C'
d['d'] = 'D'
d['e'] = 'E'

for k, v in d.items():
    print(k, v)


"""
Igualdade com um Dicionário Ordenado
Um dicionario normal olha para seu próprio conteúdo quando testa por igualdade. 
Um OrderedDict também considera a ordem em que os itens foram adicionados.
"""
# Um dicionário normal:
print('Dictionaries are equal?')

d1 = {}
d1['a'] = 'A'
d1['b'] = 'B'

d2 = {}
d2['b'] = 'B'
d2['a'] = 'A'

print(d1 == d2)