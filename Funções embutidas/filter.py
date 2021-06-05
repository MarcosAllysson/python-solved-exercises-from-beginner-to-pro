"""
* Filtrando a lista, aplico filter com função lambda verificando se o elemento é par. Caso True, adiciona à lista.
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# com lambda
print(list(filter(lambda x: x % 2 == 0, lista)))


def par(num):
    if num % 2 == 0:
        return True


# com função
print(list(filter(par, lista)))
