
class Bicicleta:
    def __init__ (self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor


    def buzinar(self):
        print("Plim, plim...")
        
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada !")

    def correr(self):
        print("Vrummmmmmmmm...")

    #def get_cor(self):
    #    return self.cor


b1 = Bicicleta("vermelha", "caloi", 2022, 600.0)

b1.buzinar()

b1.correr()

b1.parar()

print(f"A bicicleta é {b1.cor}, modelo {b1.modelo}, do ano {b1.ano} e custa R$ {b1.valor:.2f}")

b2 = Bicicleta("verde", "monark", 2000, 189.0)

print(f"A bicicleta é {b2.cor}, modelo {b2.modelo}, do ano {b2.ano} e custa R$ {b2.valor:.2f}")

Bicicleta.buzinar(b2)

b2.buzinar() # Bicicleta.buzinar(b2)

#print(b2.get_cor())
print(b2.cor)

print(b2)