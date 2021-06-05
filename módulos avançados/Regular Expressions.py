import re

# Lista de padrões para procurar
patterns = ['term1', 'term2']

# Texto para analisar
text = 'This is a string with term1, but it does not have the other term.'

for pattern in patterns:
    print(f'Searching for {pattern} in: {text}')

    # Checa por correspondencia
    if re.search(pattern, text):
        print('Match was found. ')
    else:
        print('No Match was found.')

"""
Split com expressões regulares
Vamos ver como podemos dividir com a sintaxe do re. Isso deve parecer semelhante à forma como você usou 
o método split() com strings.
"""
print()

# Termo onde realizaremos a divisão
split_term = '@'

phrase = 'What is the domain name of someone with the email: hello@gmail.com'

# Divide a frase
print(re.split(split_term, phrase))

"""
Encontrando todas as instâncias de um padrão
Você pode usar re.findall() para encontrar todas as instâncias de um padrão em uma string. Por exemplo:
"""
# Retorna uma lista de todas as correspondências
print(re.findall('match', 'test phrase match is in middle'))



"""
Sintaxe de repetição
Existem cinco maneiras de expressar a repetição em um padrão:
1.) Um padrão seguido por um metacaractere é repetido zero ou mais vezes.      
2.) Substitua o por + e o padrão deve aparecer pelo menos uma vez.      
3.) Usar ? significa que o padrão aparece zero ou uma vez.      
4.) Para um número específico de ocorrências, use {m} após o padrão, onde m é substituído pelo número 
de vezes que o padrão deve repetir.      
5.) Use {m, n} onde m é o número mínimo de repetições e n é o máximo.      
Agora, veremos um exemplo de cada um destes usando nossa função multi_re_find:
"""
def multi_re_find(patterns,phrase):
    '''
    Toma uma lista de padrões regex
    Imprime uma lista de todas as partidas
    '''
    for pattern in patterns:
        print('Searching the phrase using the re check: %r' %pattern)
        print(re.findall(pattern,phrase))
        print('\n')

test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = [ 'sd*',     # s seguido de zero ou mais d's
                'sd+',          # s seguido de um ou mais d's
                'sd?',          # s seguido por zero ou um d
                'sd{3}',        # s seguido por três d's
                'sd{2,3}',      # s seguido de dois a três d's
                ]

print(multi_re_find(test_patterns,test_phrase))



"""
Conjuntos de caracteres
Os conjuntos de caracteres são usados quando você deseja combinar qualquer grupo de caracteres na entrada. 
Os colchetes são usados para construir entradas de conjunto de caracteres. Por exemplo: a entrada [ab] 
procura as ocorrências de a ou b.
"""
test_phrase = 'sdsd..sssddd...sdddsddd...dsds...dsssss...sdddd'

test_patterns = ['[sd]',  # s ou d
                 's[sd]+']  # s seguido de um ou mais s ou d's

print(multi_re_find(test_patterns, test_phrase))


"""
Exclusão
Podemos usar ^ para excluir termos incorporando-os na notação de colchetes. Por exemplo: [^ ...] 
irá combinar qualquer caracter que não esteja nos colchetes.
"""
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
print(re.findall('[^!.? ]+',test_phrase))



"""
Intervalos de caracteres
À medida que os conjuntos de caracteres crescem, a digitação de cada caracter que deve (ou não) corresponder 
pode tornar-se muito tediosa. Um formato mais compacto usando intervalos de caracteres permite que você defina 
um conjunto de caracteres para incluir todos os caracteres contíguos entre um ponto de início e de parada. 
O formato utilizado é [inicio-fim].
"""
test_phrase = 'This is an example sentence. Lets see if we can find some letters.'

test_patterns = ['[a-z]+',  # sequências de letras minúsculas
                 '[A-Z]+',  # sequências de letras maiúsculas
                 '[a-zA-Z]+',  # sequências de letras maiúsculas ou minúsculas
                 '[A-Z][a-z]+']  # uma letra maiúscula seguida de letras minúsculas

print(multi_re_find(test_patterns, test_phrase))

