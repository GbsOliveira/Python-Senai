#listas
#em vez de fazer assim:
aluno1="Dany"
aluno2="Lucas"
aluno3="daniel"

#fazer assim:
alunos=["dany", "lucas", "daniel"]
print(alunos[1])

#adc na lista
alunos.append("gabriela")
print("adc gabriela")
print(alunos)

#remover da lista
alunos.remove("daniel")
print("removendo o daniel")
print(alunos)

#incluir um item em uma posicao especifica
alunos.insert(0, "joao")
print("Lista com o joao em primeiro")
print(alunos)

for aluno in alunos:
    print(aluno)

    #atualizando um item da lista
    alunos[0] = "lucas"
    print("atuaLIZANDO A LISTA")
    print(alunos)

    #descobrir o indice de um elemento na lista
    print(alunos.index("dany"))

    #atualizar a lista
    #alunos[alunos.index("dany")] = "beatriz"
    #print("beatriz no lugar do dany", alunos)
    #print(alunos)

    #tamanho da lista
    print("Tamanho da lista: ", len(alunos))