# Função de gerador para o cubo de números (potência de 3)
def gencubes(n):
    for num in range(n):
        yield num ** 3

# for x in gencubes(10):
#    print(x)


"""
Problema 1 - Crie um gerador que gere os quadrados de números até um número N.
"""
def gensquares(N):
    for i in range(N):
        yield i ** 2

# for x in gensquares(10):
#    print(x)


"""
Problema 2 - Crie um gerador que produza "n" números aleatórios entre um número baixo e alto (que são entradas)
"""
from random import randint

def rand_num(low, high, n):
    for i in range(n):
        yield randint(low, high)

#for num in rand_num(1, 10, 12):
#    print(num)


"""
Problema 3
Use a função iter() para converter a string abaixo
s = 'hello'
"""
s = 'hello'
s_iter = iter(s)
#for i in s:
#    print(next(s_iter))



"""
Só explicar o código...
"""
my_list = [1, 2, 3, 4, 5]
gencomp = (item for item in my_list if item > 3)
print(gencomp)
#for item in gencomp:
#    print(item)
