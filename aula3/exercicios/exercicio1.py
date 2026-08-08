"""
### Par ou ímpar

Crie um programa que:

1. Receba um número inteiro com `input()`.
2. Use `%` e uma estrutura `if` / `else`.
3. Informe se o número é par ou ímpar.

"""

num_digitado = int(input("Digite um número inteiro: "))
resto = num_digitado%2

if num_digitado ==0:
    print(f"O número {num_digitado} é par")
else:
    print(f"O número {num_digitado} é impar")