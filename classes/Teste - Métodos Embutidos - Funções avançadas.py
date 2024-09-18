"""
Problema 1
Use o map para criar uma função que encontre o tamanho de cada palavra na frase (quebrado por espaços)
e retornar os valores em uma lista.
A função terá uma entrada de uma string e exibirá uma lista de números inteiros.
word_lengths('How long are the words in this phrase')
saída: [3, 4, 3, 3, 5, 2, 4, 6]
"""
word_lengths = 'How long are the words in this phrase'
# print(list(map(lambda lista: len(lista), word_lengths.split())))


"""
Problema 2
Use reduce para pegar uma lista de dígitos e retornar o número que eles correspondem a.
Não converta os números inteiros em strings! *
digits_to_num([3,4,3,2,1])
34321
"""
from functools import reduce

digits_to_num = [3, 4, 3, 2, 1]
#print(reduce(lambda a, b: a * 10 + b, digits_to_num))


"""
Problema 3
Use o filter para retornar as palavras de uma lista de palavras que começam com uma letra especificada.
l = ['hello','are','cat','dog','ham','hi','go','to','heart']
filter_words(l,'h')
['hello', 'ham', 'hi', 'heart']
"""
lista = ['hello', 'are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
# print(list(filter(lambda palavra: palavra[0] == 'h', lista)))


"""
Problema 4
Use zip e list comprehension para retornar uma lista do mesmo comprimento onde cada valor 
é as duas cadeias de caracteres de L1 e L2 concatenados juntos com o conector entre eles. Veja o exemplo abaixo:
concatenate(['A','B'],['a','b'],'-')
['A-a', 'B-b']
"""
def concatenate(l1, l2, conector):
    return [ palavra1 + conector + palavra2 for (palavra1, palavra2) in zip (l1, l2) ]
#print(concatenate(['A','B'],['a','b'],'-'))


"""
Problema 5
Use enumerate e outras habilidades para retornar um dicionário que tenha os valores da lista 
como chaves e o índice como o valor. Você pode assumir que um valor só aparecerá uma vez na lista fornecida.
d_list(['a','b','c'])
{'a': 0, 'b': 1, 'c': 2}
"""
def d_list(lista):
    return {key:value for value, key in enumerate(lista)}
#print(d_list(['a', 'b', 'c']))

"""
Problema 6
Use enumerar e outras habilidades de cima para retornar a contagem do número de 
itens na lista cujo valor é igual ao seu índice.
count_match_index([0,2,2,1,5,5,6,10])
"""
count_match_index = [0, 2, 2, 1, 5, 5, 6, 10]
soma = cont = 0
for chave, valor in enumerate(count_match_index):
    if chave == valor:
        soma += valor
        cont += 1
#print(f'Soma: {soma}, contagem: {cont}.')

