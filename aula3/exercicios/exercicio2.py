"""
Crie um programa que:

1. Receba a idade da pessoa.
2. Informe se ela é maior ou menor de idade.
3. Se faltar pouco (`16` ou `17` anos), informe 
também quantos anos faltam para os 18.

"""
idade = int(input("Digite a sua idade: "))
if idade >=18:
    print(f"Maior de Idade")
else:
    print(f"Menor de Idade")

if 16 <= idade <=17:
    print(f"Ainda falta(m) {18-idade} ano(s) para você completar 18 anos!")