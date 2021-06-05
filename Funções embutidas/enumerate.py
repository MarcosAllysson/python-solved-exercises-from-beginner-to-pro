"""
Retorna chave e valor de um iterável, uma lista por exemplo.
"""

lista = [1, 2, 3, 4, 5, 6]
lista2 = ['fruit', 'watermelon', 'english', 'language', 'rich', 'Jesus', ]

for chave, valor in enumerate(lista2):
    print(f'\033[1;33m{chave + 1}° elemento\033[m: \033[4m{valor}...\033[m')

    if valor[0] in 'Jj':
        print(f'\033[1;33mMeu pai\033[m: \033[4m{valor}...\033[m')

