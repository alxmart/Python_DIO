
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.raca = cor
        self.acordado = acordado

    def latir(self):
        print(f'{self.nome} está latindo!')

    def dormir(self):
        self.acordado = False
        print(f'{self.nome} está dormindo!')


dog = Cachorro('Mucao', 'Vira-lata', False)

dog.latir()

dog.dormir()


