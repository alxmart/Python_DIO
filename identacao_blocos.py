
def sacar(valor: float) -> None:

    saldo = 9500.00

    if saldo >= valor:
        print("Valor sacado: ", float(valor))
        saldo -= valor
        print("Saldo: ", float(saldo))
    else:
        print("Saldo insuficiente para saque")
        print("Saldo: ", float(saldo))
        print("Valor do saque: ", float(valor))
        print("Operação não realizada")

    print("Obrigado por usar o nosso banco")


sacar(1500.00)


              
              
