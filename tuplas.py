
frutas = ("laranja", "pera", "uva",)

letras = tuple("Python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

frutas[0] # maçã

frutas[2] # uva

frutas[-1] # uva

frutas[-2] # pera

matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)

matriz[0][0] # 1

matriz[0][-1] # 2

matriz[-1][-1] # "c"


tupla = ("P", "y", "t", "h", "o", "n")

print(tupla[2:]) # ("t", "h", "o", "n")

print(tupla[:2]) # ("P", "y")

print(tupla[1:3]) # ("y", "t")

print(tupla[0:3:2]) # ("P", "t")

print(tupla[::]) # ("P", "y", "t", "h", "o", "n")

print(tupla[::-1]) # ("n", "o", "h", "t", "y", "P")


carros = ("gol", "celta", "palio",)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

"""
0: gol
1: celta
2: palio
"""

linguagens = ("python", "java", "c#", "javascript",)

linguagens.index("c#") # 2

linguagens.index("python") # 0

len(linguagens) # 4

carros = ("gol") 

print(isinstance(carros, tuple))






