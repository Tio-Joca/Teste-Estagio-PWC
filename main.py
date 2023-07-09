from collections import Counter

def reverter_ordem_palavras(frase):
    palavras = frase.split()
    palavras_revertidas = palavras[::-1]

    frase_revertida = ' '.join(palavras_revertidas)
    return frase_revertida

def remover_caracteres_repetidos(string):
    caracteres_unicos = ""

    for char in string:
        if char not in caracteres_unicos:
            caracteres_unicos += char

    return caracteres_unicos

def substring_palindroma(string):
    if len(string) < 2:
        return string

    inicio = 0
    fim = 0

    for i in range(len(string)):
        
        j = i - 1
        k = i + 1
        while j >= 0 and k < len(string) and string[j] == string[k]:
            if k - j > fim - inicio:
                inicio = j
                fim = k
            j -= 1
            k += 1

        j = i
        k = i + 1
        while j >= 0 and k < len(string) and string[j] == string[k]:
            if k - j > fim - inicio:
                inicio = j
                fim = k
            j -= 1
            k += 1

    return string[inicio:fim+1]

def maiuscula_inicial(palavra):
    return palavra.capitalize()

def maiuscula_iniciais_frase(frase):
    palavras = frase.split()

    palavras_capitalizadas = [maiuscula_inicial(palavra) for palavra in palavras]

    frase_capitalizada = ' '.join(palavras_capitalizadas)
    return frase_capitalizada

def verificador_anagrama_palindromo(string):
    string = string.lower().replace(" ", "")
    contador = Counter(string)

    count_impares = 0

    for count in contador.values():
        if count % 2 != 0:
            count_impares += 1

    if count_impares <= 1:
        return "A string é um anagrama de um palíndromo."
    else:
        return "A string não é um anagrama de um palíndromo."

entrada = input("Digite uma frase: ")

frase_revertida = reverter_ordem_palavras(entrada)
print("Frase revertida:", frase_revertida)

string_caracteres_unicos = remover_caracteres_repetidos(entrada)
print("String sem caracteres duplicados:", string_caracteres_unicos)

substring_palindroma = substring_palindroma(entrada)
print("Substring palíndroma mais longa:", substring_palindroma)

frase_capitalizada = maiuscula_iniciais_frase(entrada)
print("Frase com as primeiras letras maiúsculas:", frase_capitalizada)

resultado_anagrama_palindromo = verificador_anagrama_palindromo(entrada)
print(resultado_anagrama_palindromo)
