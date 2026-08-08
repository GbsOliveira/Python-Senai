"""
Crie um programa que:

1. Receba duas notas decimais e calcule a média (com parênteses).
2. Use `if` / `elif` / `else` para classificar:
    - média `>= 6` → Aprovado;
    - média entre `4` e `5.9` → Recuperação;
    - média `< 4` → Reprovado.
3. Exiba a média com uma casa decimal e a situação.

"""

aluno = input("Nome do Aluno: ")


nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

media = (nota1 + nota2) / 2
print(f"A média de {aluno} é: {media:.2f}")

if media >= 6:
    print(f"{aluno} está Aprovado")
elif 4 <= media < 6:
    print(f"{aluno} está de Recuperação")
else:
    print(f"{aluno} está Reprovado")