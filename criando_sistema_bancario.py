
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

# DEPÓSITO
    if opcao == "d":

        valor = float(input("Informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito efetuado no valor de R$ {valor: .2f}\n"
        else:
            print("Operação Cancelada ! Valor inválido.")

# SAQUE
    elif opcao == "s":

        valor = float(input("Informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Cancelada ! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação Cancelada ! Valor do saque excede o valor limite por saque.")
        
        elif excedeu_saques:
            print("Operação Cancelada ! O número máximo de saques diários foi excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque efetuado no valor de R$ {valor: .2f}\n"
            numero_saques += 1
        
        else:
            print("Operação Cancelada ! Valor inválido.")

# EXTRATO
    elif opcao == "e":
        print("\n------- Extrato --------")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo: .2f}")
        print("------------------------")

# SAíDA
    elif opcao == "q":
        break

# OPERAÇÃO INVÁLIDA
    else:
        print("Operação inválida !  Por favor, selecione a operação desejada.")