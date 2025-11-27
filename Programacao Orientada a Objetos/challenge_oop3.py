"""
Descrição
Implemente uma classe ConversorTemperatura que converte temperaturas de Celsius para Fahrenheit. A classe deve incluir um método chamado celsius_para_fahrenheit que realiza o cálculo de conversão. A fórmula para converter de Celsius para Fahrenheit é:

Fahrenheit=(Celsius×95)+32Fahrenheit=(Celsius×59​)+32

Você também deverá criar uma instância do conversor e utilizar essa instância para realizar a conversão.

Documentação Oficial:
https://docs.python.org/pt-br/3/tutorial/classes.html

https://docs.python.org/pt-br/3/library/stdtypes.html#methods

Entrada
O programa deverá receber como entrada uma temperatura em graus Celsius fornecida pelo usuário.

Saída
O programa deverá exibir a temperatura convertida para Fahrenheit.
"""

#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:

class ConverteTemperatura:
    def celsius_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit

# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = ConverteTemperatura()

fahrenheit = conversor.celsius_fahrenheit(celsius)
print(fahrenheit)
