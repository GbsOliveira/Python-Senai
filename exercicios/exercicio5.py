nome_prod = input("Informe o nome do produto: ")
qntd = int(input("Informe a quantidade do produto: "))
preco_unit = float(input("Qual o preço da unidade: "))

total = qntd*preco_unit
print(f"Produto:\t{nome_prod}\nQuantidade:\t{qntd}\nTotal: R$\t{total:.2f}\n")

