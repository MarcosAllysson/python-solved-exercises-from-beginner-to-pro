"""
Problema 1
Manuseie a exceção lançada pelo código abaixo usando os blocos try e except.
"""

"""
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)
except TypeError:
    print('Use apenas valores inteiros! ')
"""


"""
Problema 2
Manuseie a exceção gerada pelo código abaixo usando os blocos try e except. 
Em seguida, use um bloco finally para imprimir 'All Done'.
"""
x = 5
y = 0
"""
try:
    z = x / y
except ZeroDivisionError:
    print('Não é possível divisão por 0')
finally:
    print('All Done')
"""



"""
Problema 3
Escreva uma função que solicite um número inteiro e imprima o quadrado dele. 
Use um loop while com um try, except e else para contabilizar as entradas incorretas.
"""
from math import pow


def ask():
    entradas_incorretas = 0
    while True:
        try:
            num = int(input('Informe um número: '))
            quadrado = pow(num, 2)
        except Exception as error:
            print(f'Erro: {error.__class__}, descrição: {error}.\nTenta de novo!')
            entradas_incorretas += 1
        else:
            print(f'Tudo certo! {num} ao quadrado é {quadrado}.')
            if entradas_incorretas > 0:
                print(f'Entradas inválidas: {entradas_incorretas}')
            break

ask()
