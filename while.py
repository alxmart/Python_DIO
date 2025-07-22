

import sys

opcao = -1

saldo = 25000.00

while opcao != 0 and opcao != 4:
    print("Informe uma opção: \n [1] Sacar \n [2] Extrato \n [3] Depositar \n [4] Sair \n")
    opcao = int(input())

    if opcao == 1:        
        saque = float(input("Informe o valor do saque: "))
        if saldo >= saque:
            saldo -= saque
            print("Saque efetuado com sucesso!")
            print("Saldo atual: R$ %.2f" % saldo)
        else:
            print("Saldo insuficiente!")
    elif opcao == 2:    
        print("Extrato: R$ %.2f" % saldo)
    elif opcao == 3:
        deposito = float(input("Informe o valor do depósito: "))
        saldo += deposito
        print("Depósito efetuado com sucesso!")
        print("Saldo atual: R$ %.2f" % saldo)
    elif opcao == 4:
        print("Sistema encerrado!")
    else:
        sys.exit("Opção inválida")