"""
Crie um programa que:

1. Receba peso (kg) e altura (m).
2. Calcule o IMC com `peso / altura ** 2`.
3. Use `elif` para classificar: abaixo do peso (`< 18.5`), peso normal (`< 25`), sobrepeso (`< 30`) e obesidade (`>= 30`).
4. Exiba o IMC com duas casas decimais.

"""

peso = float(input(f"Informe seu peso em kilos: "))
altura = float(input(f"Informe sua altura em metros: "))

imc = peso / (altura**2)

if imc < 18.5:
    print(f"Você esta abaixo do peso")
elif imc < 25:
    print(f"Seu peso esta normal")
elif imc < 30:
    print(f"Você está com sobrepeso")
elif imc >=30:
    print(f"Você esta com obesidade")
