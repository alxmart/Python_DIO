
dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria" # Sobrepõe o valor da chave "nome"
dados["idade"] = 18 # Sobrepõe o valor da chave "idade"
dados["telefone"] = "9988-1781" # Sobrepõe o valor da chave "telefone"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
