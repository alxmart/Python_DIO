 
while True:
    try:
        numero = int(input("Informe um número positivo: "))
        if numero < 0:
            print("Número informado é negativo, encerrando o loop.")
            break
        else:
            print(f"Número informado: {numero}")
    except ValueError:
        print("Entrada inválida, por favor informe um número inteiro para continuar.")