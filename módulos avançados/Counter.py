from collections import Counter

# Counter() com listas
l = [1, 2, 2, 2, 2, 3, 3, 3, 1, 2, 1, 12, 3, 2, 32, 1, 21, 1, 223, 1]
print(Counter(l))

# Counter com strings
print(Counter('aabsbsbsbhshhbbsbs'))

#Counter com palavras em uma sentença.
s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
print(Counter(words))

# Métodos com Counter()
c = Counter(words)
print(c.most_common(2))


