"""
O zip() basicamente agrega / junta 2 iteráveis em uma lista de tuplas.
Onde cada índice recebe os elementos correspondentes dos iteráveis
"""
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

agregacao_zip = list(zip(lista1, lista2))
print(agregacao_zip)
