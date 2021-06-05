import datetime

t = datetime.time(4, 20, 1)
# Vamos mostrar as diferenças entre os componentes

print(t)
print('hour  :', t.hour)
print('minute:', t.minute)
print('second:', t.second)
print('microsecond:', t.microsecond)
print('tzinfo:', t.tzinfo)

print()
print('Earliest  :', datetime.time.min)
print('Latest    :', datetime.time.max)
print('Resolution:', datetime.time.resolution)


"""
Dates
O tempo de data (como você talvez tenha suspeitado) também nos permite trabalhar com timestamps de data. 
Os valores da data do calendário são representados com a classe de data. As instâncias possuem atributos 
por ano, mês e dia. É fácil criar uma data que represente a data de hoje usando o método de classe today().
"""
today = datetime.date.today()
print()
print(today)
print('ctime:', today.ctime())
print('tuple:', today.timetuple())
print('ordinal:', today.toordinal())
print('Year:', today.year)
print('Mon :', today.month)
print('Day :', today.day)



"""
Operações aritméticas
Podemos realizar operações aritmética em objetos de data para verificar diferenças horárias. Por exemplo:
"""
d1 = datetime.date(2015, 3, 11)
d2 = datetime.date(1990, 3, 11)
print()
print(d1-d2)
