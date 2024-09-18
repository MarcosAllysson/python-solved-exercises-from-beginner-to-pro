"""
Números avançados
Problema 1: Converta 1024 para a representação binária e hexadecimal:
"""
num = 1024
print(f'{num} em Representação binária: {bin(num)[2:]}')
print(f'{num} em Representação hexadecimal: {hex(num)[2:]}')


"""
Problema 2: Arredonde 5.23222 para duas casas decimais
"""
print(round(5.23222, 2))
print(f'{5.23222:.2f}')


"""
Problema 3: Verifique se cada letra na seqüência "s" é minúscula
"""
s = 'hello how are you Mary, are you feeling okay?'
min = []
mai = []
for i in s:
    if i.islower():
        min.append(i)
    elif not i.islower():
        if i.isalpha():
            mai.append(i)
print(f'Minúscula: {min}')
print(f'Maiúscula: {mai}')


"""
Problema 4: quantas vezes a letra 'w' aparece na string abaixo?
"""
from collections import Counter
s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'
cont = 0
print(f'Com counter: {Counter(s)["w"]}, vezes')
for letra in s:
    if letra in 'Ww':
        cont += 1
print(f'Letra "w" aparece {cont} vezes na string.')
lista = list(filter(lambda letra: letra == 'w', s))
print(f'Com filter e função lambda: "w" aparece {len(lista)} na lista.')
print(f'Com count da string: {s.count("w")} vezes')


"""
Problema 5: Encontre os elementos no set1 que não estão no set2:
"""
set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print(set1.difference(set2))


"""
Problema 6: Encontre todos os elementos que estão no conjunto:
"""
print(set1.union(set2))


"""
Problema 7: Crie este dicionário: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64}   usando compreensão.
"""
dicio = {x:x**3 for x in range(5)}
print(dicio)


"""
Problema 8: Inverta a lista abaixo:
"""
l = [1,2,3,4]
l.reverse()
print(l)
#print(l[::-1])



"""
Problema 9: Classifique (ordenar) a lista abaixo
"""
l = [3,4,2,5,1]
l.sort()
print(l)
