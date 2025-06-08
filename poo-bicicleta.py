
class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print(f'{self.modelo} está buzinando !')

    def parar(self):

        print(f'{self.modelo} está parando !')
    
    def correr(self):
        
        print(f'{self.modelo} está correndo !')

    """
    def __str__(self):
        return f'Bicicleta: modelo: {self.modelo}, cor:{self.cor}, ano:{self.ano}, Valor:{self.valor}'
    """

    def __str__(self):
        #return f"{self.__class__.__name__}({self.cor}, {self.modelo}, {self.ano}, {self.valor})"
        return f"{self.__class__.__name__}"


bike1 = Bicicleta('Azul', 'Caloi Cross', 2020, 500)

bike1.buzinar()
bike1.correr()
bike1.parar()

print("Minha bike:")
print("Modelo:", bike1.modelo)
print("Cor:", bike1.cor)
print("Ano:", bike1.ano)
print("Valor:", bike1.valor)

print("Exibindo instância")
print(bike1)


