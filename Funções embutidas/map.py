# Criamos uma pequena expressão para converter Fahrenheit a Celsius
def fah(temperatura):
    return (9 / 5) * temperatura + 32


def cel(temperatura):
    return (5 / 9) * (temperatura - 32)


temp = [0, 22.5, 40, 100]

# aplicando o map e convertendo pra fah
fah_temps = list(map(fah, temp))
print(fah_temps)

# map convertendo de volta pra celcius
cel_temps = list(map(cel, fah_temps))
print(cel_temps)


# No exemplo acima, não usamos uma expressão lambda.
# Ao usar lambda, não teríamos que definir e nomear as funções fahrenheit() e celsius().
com_lambda = list(map(lambda x: (5.0 / 9) * (x - 32), fah_temps))
print(com_lambda)
