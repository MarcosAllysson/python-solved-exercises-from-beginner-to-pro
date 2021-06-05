"""
Reduce aplica uma função a todos os elementos iteráveis até retornar apenas 1 elemento - REDUZIR
"""
from functools import reduce

lista = [47, 11, 42, 13]
print(reduce(lambda a, b: a + b, lista))
print(reduce(lambda a, b: a * b, lista))

"""
 Maior elemento da lista
 Função lambda recebe 2 parâmetros, retorna A se A > B, se não retorna B
 Printando juntamente com reduce, chamando a função e passando a lista anterior como parâmetro
"""
max_element = lambda a, b: a if (a > b) else b
print(reduce(max_element, lista))
