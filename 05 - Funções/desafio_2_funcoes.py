 
# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:
def elementos_comuns(lista1_str, lista2_str):
    # Converte as listas de strings para conjuntos de inteiros para encontrar os elementos comuns
    set1 = set(map(int, lista1_str))
    set2 = set(map(int, lista2_str))
    return list(set1.intersection(set2))

# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")

    """
    Resultado Execução:

    1 2 3 4 
    5 6 7 3
    Elementos comuns às duas listas: [3]
    """