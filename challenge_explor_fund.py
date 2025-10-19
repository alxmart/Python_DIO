
"""
numero = int(input())

if numero % 2 == 0:
    print("Par")
else: 
  print("Impar")
"""

#------------------------------------------------------------


"""
def verificador_ano_bissexto():
    ano = int(input())

# TODO: Verifique se o ano é bissexto utilizando uma estrutura de controle condicional, como if/else:
    
    if  ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("SIM")
    else:
        print("NÃO")

verificador_ano_bissexto()
"""

#-----------------------------------------------------------
    
def conta_vogais(texto):
    # TODO: Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = "aeiouAEIOU"
    
    # TODO: Inicialize um contador para contar as vogais:
    contador = 0
    
    
    # Iteramos pelos caracteres da string
    for char in texto:
        # TODO: Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
          contador += 1
        
    
    return contador

# Solicitamos ao usuário que insira uma string
texto = input()

# Chamamos a função conta_vogais e exibimos o resultado
resultado = conta_vogais(texto)
print(f"O número de vogais na string '{texto}' é: {resultado}")