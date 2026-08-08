"""
Crie um programa que:

1. Receba dois números e o símbolo da 
operação (`+`, `-`, `*`, `/`).
2. Use `if` / `elif` para executar a operação 
escolhida.
3. Trate dois casos especiais: **divisão por zero**
 e **operação inválida**.

"""
print("\n-----CALCULADORA-----\n")
      
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

print("\nEscolha a operação: ")
operacao = input("\nDigite o símbolo da operação (+, -, *, /): ")

#print(f"{num1}, {num2} e {operacao}")
if operacao == "+":
     resultado = num1 + num2
     print(f"O valor da operação é: {resultado}")
elif operacao == "-":
     resultado = num1 - num2
     print(f"O valor da operação é: {resultado}")
elif operacao == "*":
     resultado = num1 * num2
     print(f"O valor da operação é: {resultado}")
elif operacao == "/":
     resultado = num1 / num2
     print(f"O valor da operação é: {resultado}")
else:
     print("Operação inválida.")