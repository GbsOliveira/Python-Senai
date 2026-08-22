
alunos = int(input("Informe a quantidade de alunos: "))

for x in range(alunos): 
    
    nota1 = float(input("Informe a nota 1: "))
    nota2 = float(input("Informe a nota 2: "))
    nota3 = float(input("Informe a nota 3: "))
    nota4 = float(input("Informe a nota 4: "))

    if alunos !=0:
        media = (nota1+nota2+nota3+nota4)/4
        print(f"A media da turma é: {media} ")
    else:
        print(f"quantidade inválida")
         

    #forma mais enxuta
    #alunos = int(input("Informe a quantidade de alunos: "))
    #soma_notas=0

        #for x in range(alunos):
            #nota_recebida = float(input(f"nota do aluno [x]: ")) recebe as notas
            #soma_notas = soma_notas + nota_recebida  atualiza a soma

        #if alunos != 0:
            #media = soma_notas / alunos
            #print(f"media da turma: {media}"")
        #else:
            #print(f"Quantidade invalida!")





   