from collections import defaultdict

d = {}
#print(d['one'])

d  = defaultdict(object)
print(d['one'])

for item in d:
    print(item)

#Também pode inicializar com valores padrão:
d = defaultdict(lambda: 0)
print(d['one'])
