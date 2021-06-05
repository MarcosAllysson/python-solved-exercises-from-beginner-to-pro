# Exemplo 1 - # Pega todas as letras em uma string
lst = [x for x in 'word']
#print(lst)

# Exemplo 2 - Eleva o quadrado itens no range e o transformam em lista
lst = [x**2 for x in range(0,11)]
#print(lst)

# Exemplo 3 - # Cria uma lista de números pares, utilizando para isso o if
lst = [x for x in range(11) if x % 2 == 0]
#print(lst)

# Exemplo 4 - Converte Celsius para Fahrenheit
celsius = [0,10,20.1,34.5]
fahrenheit = [ ((float(9)/5)*temp + 32) for temp in celsius]
#print(fahrenheit)

# Exemplo 5 - Também podemos realizar compreensões de lista aninhadas, por exemplo:
lst = [ x**2 for x in [x**2 for x in range(11)]]
#print(lst)
