
# OLD:
nome = "Homer"
idade = 39
profissao = "Engenheiro de Seguranca"

print("Olá, me chamo %s, tenho %d anos e trabalho como %s." % (nome, idade, profissao)) 
# %s p/ string, %d p/ int, %f p/ float

# OLD2 - Método Format:
print("Olá, me chamo {}, tenho {} anos e trabalho como {}.".format(nome, idade, profissao))

print("Olá, me chamo {0}, tenho {1} anos e trabalho como {2}.".format(nome, idade, profissao))

print("Olá, me chamo {name}, tenho {age} anos e trabalho como {work}.".format(name=nome, age=idade, work=profissao))

# print("Olá, me chamo {nopme}, tenho {idade} anos e trabalho como {profissao}.".format(**pessoa))

# F-STRING:
print(f"Hello, me chamo {nome}, tenho {idade} anos e trabalho como {profissao}.")

# FORMATANDO VALORES COM F-STRINGS:

pi = 3.14159

print(f"O valor de pi é aproximadamente {pi: .2f}.")  # Duas casas decimais      

print(f"O valor de pi é aproximadamente {pi: 10.2f}.")  

print(f"O valor de pi é aproximadamente {pi: .4f}.")  # Quatro casas decimais







