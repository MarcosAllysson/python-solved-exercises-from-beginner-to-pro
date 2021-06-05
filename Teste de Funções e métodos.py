# Escreva uma função que calcula o volume de uma esfera dado seu raio.
# Ve = 4 * pi * r³/ 3
def vol(rad):
    return f'{4 * 3.14 * rad ** 3 / 3:.2f}cm³'
# print(vol(5))


# Escreva uma função que verifica se um número está em um determinado intervalo (inclusive o máximo e mínimo)
def ran_check(num,low,high):
    # com expressão lambda
    intervalo = lambda num: num >= low and num <= high
    return intervalo(num)
    
    # com verificação maior
    # if num >= low and num <= high:
    #     return True
    # else:
    #     return False

    # com verificação no for
    # if num in range(low, high+1):
    #     return True
    # else:
    #     return False
        
# print(ran_check(4, 0, 10))
# print(ran_check(12, 0, 10))



# Escreva uma função Python que aceita uma string e calcule o número de maiúsculas e minúsculas.
#Exemplo de Cadeia: 'Olá Sr. Rogers, como você está bem, terça-feira?'
# Saída esperada: Número de caracteres maiúsculas: 3
# Número de caracteres minúsculos: 33
def up_low(s):
    """
    A partir da string, uso for para varrer a string pra verificar cada letra usando métodos isupper() e islower()
    Retorna uma lista aninhada, onde o índice 0 recebe as minúsculas e o índice 1, maiúsculas.
    """
    cadeia = [[], []]
    for letra in s:
        if letra.islower():
            cadeia[1].append(letra)
        elif letra.isupper():
            cadeia[0].append(letra)

    return f'Número de caracteres maiúsculas: {len(cadeia[0])} \nNúmero de caracteres minúsculos: {len(cadeia[1])}'

# print(up_low('Olá Sr. Rogers, como você está bem, terça-feira?'))
#help(up_low)



# Escreva uma função Python que recebe uma lista e retorna uma nova lista com elementos exclusivos da primeira lista.
# Lista de Amostras: [1,1,1,1,2,2,3,3,3,3,4,5]
# Lista única: [1, 2, 3, 4, 5]
def unique_list(l):
    """
    Retornando set() da lista recebida como parâmetro
    """
    return list(set(l))
    
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))



# Escreva uma função Python para multiplicar todos os números em uma lista.
# Lista de exemplos: [1, 2, 3, -4]
# Saída esperada: -24
def multiply(numbers):  
    numeros_multiplicados = 1
    for i in numbers:
        numeros_multiplicados *= i
    
    return numeros_multiplicados

# print(multiply([1, 2, 3, -4]))



#Escreva uma função Python que verifica se uma string passada é palindrome ou não.
#Nota: Um palíndromo é palavra, frase ou seqüência que lê o mesmo para trás.
def palindrome(s):
    """
    Verifico se a string é igual a string lendo de trás pra frente usando fatiamento de string
    Usando função lambda, recebe uma string como parâmetro já transformando os caracteres em minúsculos,
    e tirando os espaços da direita e da esquerda.
    """
    # COM FUNÇÃO LAMBDA
    palindromo = lambda string: string == string[::-1]
    return palindromo(s.lower().strip())

    # COM IF-ELSE
    # reverso = s[::-1]
    # if reverso == s:
    #     return True
    # else:
    #     return False

# print(palindrome('helleh'))
# print(palindrome('marcos'))



# Escreva uma função Python para verificar se uma string é um pangrama ou não.
# Nota: Pangramas são palavras ou frases contendo cada letra do alfabeto pelo menos uma vez.
# Dica: veja o módulo de strings
# from string import ascii_lowercase
import string

def ispangram(str1, alphabet=string.ascii_lowercase):  
    """
    Pra cada letra do alfabeto, verifico se consta na string recebida
    Se tiver, contador é somado +1
    Ao final, verificado se o contador é igual ao tamanho do alfabeto
    Se for igual, quer dizer que a string tem pelo menos 1 letra do alfabeto
    """
    num = len(alphabet)
    cont = 0

    for letra in alphabet:
        if letra in str1:
            cont += 1

    return cont == num
    
# print(ispangram("The quick brown fox jumps over the lazy dog"))
# print(ispangram("The quick"))