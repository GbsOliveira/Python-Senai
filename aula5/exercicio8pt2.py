"""
Um supermercado quer um caixa simples para registrar produtos e calcular o total da 
compra. Crie um programa que:

1. Comece com um **comentário de várias linhas** informando título do programa, 
autor e objetivo.
2. Separe o código com comentários de uma linha nas etapas **Entrada**, **
Processamento** e **Saída**.
3. Receba com `input()`:
    - nome do cliente (`str`, padronizado com `.strip().title()`);
    - quantidade de produtos diferentes (`int`).
4. Se a quantidade de produtos for menor
 ou igual a zero, exiba uma mensagem de
erro 
e encerre a lógica principal.
5. Para cada produto, receba:
    - nome do produto (`str`);
    - preço unitário (`float`);
    - quantidade comprada (`int`).
6. Use um laço para calcular o subtotal de cada produto e acumular o total da compra.
7. Conte quantos produtos tiveram subtotal maior ou igual a `50`.
8. Ao final, aplique desconto usando `if` / `elif` / `else`:
    - total `>= 300` → 10%;
    - total `>= 150` → 5%;
- abaixo de `150` → sem desconto.
9. Calcule o valor final.
10. Exiba o comprovante em **um único** `print()`, usando f-string com `\n` para 
as linhas, `\t` para alinhar e `:.2f` nos valores decimais.
11. Mostre também a quantidade de produtos com subtotal maior ou igual a `50`.

"""

#Título: Caixa Supermercado
#Autor: Gabriela 

print("------------------")
print("Caixa Supermercado")
print("------------------")
#cliente = str(input("Nome do Cliente: "))
qtdeProduto = int(input("Quantidade de Produtos: "))
#produto = str(input("Produto: "))
precoUnit = float(input("Preço Unitário: "))

while qtdeProduto<=0:
    print("Erro")
    break

for x in range(qtdeProduto):
    total = qtdeProduto * precoUnit
    print(total)

if total >= 300:
    totaldesc = total - (10/100)
elif total >= 150:
    totaldesc = total - (5/100)
    print(f"Valor final: {totaldesc}")
else: 
    print(" sem desconto ")

