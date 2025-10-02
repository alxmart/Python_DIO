

def salvar_carros(marca, modelo, ano, placa):

    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "placa": placa
    }

    return carro

salvar_carros("Ford", "Ka", 2020, "ABC-1234")
print(salvar_carros("Ford", "Ka", 2020, "ABC-1234"))

