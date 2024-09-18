#Escreva uma breve descrição de todos os seguintes tipos de objetos e estruturas de dados sobre os quais aprendemos:
"""
print(f'\033[36mNúmeros\033[m: em python, temos basicamente 2 tipos - inteiros e floats -> int(), float()')
print(f'\033[36mStrings\033[m: são caracteres de textos')
print(f'\033[36mListas\033[m: formado por diferentes tipos de valores, acessados por índices e que pode ser alterados')
print(f'\033[36mTuplas\033[m: é uma variável composto, ou seja, aceita valores valores. E são imutáveis')
print(f'\033[36mDicionários\033[m: é uma estrutura que permite ser criado por chaves e valores - dicio = dict()')
"""


#Números: Escreva uma equação que use multiplicação, divisão, expoente, adição e subtração igual a 100,25.
# print((20000 - (10 ** 2) / 10 * 35) - 19549.75)


#Strings - Dada a string 'hello', dê um comando de índice que retorna 'e'. Use o código abaixo:
# s = 'hello'
#print(s[1])

#Inverta a string 'hello' usando indexação:
#print(s[::-1])

#Dado o exemplo de linha, dê dois métodos para produzir a letra 'o' usando a indexação.
#print(s[-1])
#print(s[4])


#Listas - Crie esta lista [0,0,0] duas formas diferentes.
# lista = [0, 0, 0]
# lista2 = list()
# lista3 = []
# lista2.append(0)
# lista2.append(0)
# lista2.append(0)
# lista3.append(0)
# lista3.append(0)
# lista3.append(0)
# print(f'Lista 1: {lista};\nLista 2: {lista2};\nLista 3: {lista3}. ')

#Altere o 'hello' da lista para 'goodbye'
# l = [1,2,[3,4,'hello']]
# l[2][2] = 'goodbye'
# print(l)

#Ordene a lista:
# l = [5,3,4,6,1]
# l.sort()
# print(l)


#Dicionários - Usando chaves e indexação, pegue o 'hello' dos seguintes dicionários:
# d = {'simple_key':'hello'}
# print(d.values())
# print(d['simple_key'])

# d = {'k1':{'k2':'hello'}}
# print(d['k1']['k2'])

# d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# print(d['k1'][0]['nest_key'][1])

# d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
# print(d['k1'][2]['k2'][1]['tough'][2])


#Conjuntos - Use um conjunto para encontrar os valores exclusivos da lista abaixo:
# l = [1,2,2,33,4,4,11,22,3,3,2]
# new_list = set(l)
# print(new_list)

