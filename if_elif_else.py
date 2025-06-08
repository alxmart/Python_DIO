"""
saldo = 2000.00

saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Realizando o saque")
    saldo -= saque
    print("Saldo atual: R$ %.2f" %saldo)
else:
    print("Saldo insuficiente")
    print("Saldo atual: R$ %.2f" %saldo)
"""

"""
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:    
    saldo = saldo - saque
    print("Saque efetuado com sucesso!")
    print("Saldo atual: R$ %.2f" % saldo)
elif saldo < saque:
    print("Saldo insuficiente!")
else:
    #print("Valor inválido!")
    sys.exit("Opção inválida")
"""

saldo = 2000.00

opcao = int(input("Informe uma opção: \n [1] Sacar \n [2] Extrato \n [3] Depositar \n [4] Sair \n"))

if opcao == 1:        
    saque = float(input("Informe o valor do saque: "))
    if saldo >= saque:
        saldo = saldo - saque
        print("Saque efetuado com sucesso!")
        print("Saldo atual: R$ %.2f" % saldo)
    else:
        print("Saldo insuficiente!")
elif opcao == 2:    
    print("Extrato: R$ %.2f" % saldo)
elif opcao == 3:
    deposito = float(input("Informe o valor do depósito: "))
    saldo = saldo + deposito
    print("Depósito efetuado com sucesso!")
    print("Saldo atual: R$ %.2f" % saldo)
elif opcao == 4:
    print("Sistema encerrado!")
else:
    #print("Opção inválida!")
    sys.exit("Opção inválida")

