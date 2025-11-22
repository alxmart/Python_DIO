
def contar_caracteres(string):
    #TODO: Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.:
    contador = {}
    #TODO: Itere através de cada caractere na string string.
    for char in string:
    #TODO: Para cada caractere, verifique se ele já está presente no dicionário contador:
        if char in contador:
            contador[char] += 1
        else:
            contador[char] = 1
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)

"""

    Resultado da Execução:

    collections
    {'c': 2, 'o': 2, 'l': 2, 'e': 1, 't': 1, 'i': 1, 'n': 1, 's': 1}

"""