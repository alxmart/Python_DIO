
def sacar(valor: float) -> None:

    saldo = 9500.00

    if saldo >= valor:
        print("Valor sacado: R$ %.2f" % valor)
        saldo -= valor
        print("Saldo: R$ %.2f" % saldo)
    else:
        print("Saldo insuficiente para saque")
        print("Saldo: R$ %.2f"  %saldo)
        print("Valor do saque: R$ %.2f"  % valor)
        print("Operação não realizada")

    print("Obrigado por usar o nosso banco\n")


sacar(1500.00)


              
              
