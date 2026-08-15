"""
Crie um programa que:

1. Defina a função `celsius_para_fahrenheit(c)` 
usando a fórmula `c * 9 / 5 + 32`.
2. Receba uma temperatura em Celsius.
3. Exiba o valor convertido com uma casa decimal.
"""
#Funções
def celsius_para_fahrenheit(c):
    f = c * 9 / 5 + 32
    return f

#Entrada
print("----Conversão de Temperatura----")
celsius = float(input("Digite a temperatura em Celsius: "))

#Processamento 
fahrenheit = celsius_para_fahrenheit(celsius)

#Saída
print(f"Temperatura em °F = {fahrenheit:.1f}")
print("--------------------------------")
