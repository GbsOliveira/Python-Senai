lista_chamada = ["Vinicius", "Gabriela", "Dany", "Beatriz"]

nome = input("Chame um nome: ")

try:
    print(f"O {nome} está em {lista_chamada.index(nome)+1}º na lista")
except ValueError:
    print("O Nome não consta na lista")


posicao = int(input("Informe uma posição da lista: "))

try:
    print(f"Neste lugar, está o {lista_chamada[posicao-1]}")
except IndexError:
    print("Não tem ninguém nesta posição")