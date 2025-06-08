nome = input("Inforne o seu nome")

print(f"I'm the greatest {nome}")

# Print - Argumentos opcionais: sep, end, file, flush

print("Hello", "World", sep=" ", end="!", file=None, flush=False)

nome2 = "Homer"
sobrenome2 = "Simpson"

print(nome, sobrenome2)
print(nome2, sobrenome2, end="...\n")
print(nome2, sobrenome2, sep="#")

