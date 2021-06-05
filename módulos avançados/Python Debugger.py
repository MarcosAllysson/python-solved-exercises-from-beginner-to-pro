# Aqui vamos criar um erro de propósito, tentando adicionar uma lista a um número inteiro
import pdb

x = [1,3,4]
y = 2
z = 3

result = y + z
print(result)

# Usa o método set_trace() para pausar o código neste ponto.
pdb.set_trace()

result2 = y+x
print(result2)
