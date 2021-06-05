"""
Basicamente retorna o resultado booleano.
Com all(), retorna True se TODAS as verificações forem verdadeiras.
Com any(), retorna True se pelo menos UMA verificação for verdadeira.
"""

lista_true = [True, True, True, True, True]
lista_false = [True, True, True, True, False]
lista_false2 = [False, False, False, False, False]

# Retorna True se todos os booleanos da lista_true forem verdadeiro.
"""
print(all(lista_true))
print(all(lista_false))
print(all(lista_false2))
"""

# Retorna True se pelo menos um booleano da lista_true for verdadeiro.
"""
print()
print(any(lista_true))
print(any(lista_false))
print(all(lista_false2))
"""


# Verificando se todos ou apenas 1 elemento das listas são pares, usando all() e any() juntamente com map()
par = list(range(2, 14, 2))
imp = list(range(1, 15, 2))
result = all(map(lambda x: x % 2 == 0, par))
result2 = any(map(lambda x: x % 2 == 0, imp))
print(result)
print(result2)
