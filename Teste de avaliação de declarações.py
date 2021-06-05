# Use for, split() e if para criar uma declaração que imprima as palavras que começam com 's':
st = 'Print only the words that start with s in this sentence'
# USANDO FOR, SPLIT E IF - VERIFICAÇÃO COMUM
# palavras = list()
# for palavra in st.split():
#     if palavra[0] in 'sS':
#         palavras.append(palavra)
# print(f'Palavras que começam com S: {palavras}')


# USANDO COMPREENSÃO EM LISTA:
""" 
    RACIONAL:
        'palavras' recebe uma lista
        Usando método split() pra quebrar a lista 'st' nos espaços em branco. Passo a ter uma lista de palavras
        E pra cada palavra da minha string 'st', checa se a primeira letra - índice 0 é igual a S ou s
        Se for, adiciona à lista 'palavras'
"""
palavras = [ palavra for palavra in st.split() if palavra[0] in 'Ss' ]
#print(palavras)





# Use range() para imprimir todos os números pares de 0 a 10.
# OPÇÃO 1:
pares = list(range(0, 10, 2))
#print(pares)

# OPÇÃO 2 - for e while:
lista1 = list()
lista2 = []
for i in range(0, 10, 2):
    lista1.append(i)

cont = 0
while cont < 11:
    if cont % 2 == 0:
        lista2.append(cont)
    cont += 1
# print(f'Com for: {lista1}')
# print(f'Com while: {lista2}')

# OPÇÃO 3 - Compreensão em lista:
#pares = [ numero for numero in range(0, 10) if numero % 2 == 0]
pares = [ numero for numero in range(0, 10, 2)]
#print(pares)





# Use a compreensão de lista para criar uma lista de todos os números entre 1 e 50 que são divisíveis por 3.
div_por_3 = [ numero for numero in range(1, 50) if numero % 3 == 0 ]
#print(div_por_3)





#Percorra a string abaixo e se o comprimento de uma palavra for par imprima "é par!"
st = 'Print every word in this sentence that has an even number of letters'
# OPÇÃO 1 - USANDO FOR
# for palavra in st.split():
#     if len(palavra) % 2 == 0:
#         print(f'\033[36m{palavra}\033[m, é par...')

# OPÇÃO 2 - COMPREENSÃO EM LISTA
palavra_par = [ palavra for palavra in st.split() if len(palavra) % 2 == 0 ]
#print(palavra_par)





# Escreva um programa que imprima os números inteiros de 1 a 100. Para múltiplos de três 
# imprima "Fizz" ao ivés do número, e para os múltiplos de cinco imprima "Buzz". 
# Para números que são múltiplos de três e cinco imprima "FizzBuzz".
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)





# Use Compreensão em listas para criar uma lista das primeiras letras de cada palavra na string abaixo:
string = 'Create a list of the first letters of every word in this string'
primeiras_letras = [ palavra[0] for palavra in string.split() ]
# print(primeiras_letras)