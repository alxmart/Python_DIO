def exibir_msg():
    print("Mensagem exibida")

def exibir_msg2(nome):
    print(f"Olá, {nome}!")

def exibir_msg3(nome="Usuário"):
    print(f"Olá, {nome}!")



exibir_msg()

exibir_msg2("Homer")

exibir_msg3()

exibir_msg3("Bart")