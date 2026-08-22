import random

numero_secreto = random.randint(0, 100)

tentativas = 0
palpite = None

while palpite != numero_secreto:
    palpite = int(input("Digite um palpite entre 0 e 100: "))
    tentativas += 1

    if palpite < numero_secreto:
        print("O número secreto é maior que o palpite.")
    elif palpite > numero_secreto:
        print("O número secreto é menor que o palpite.")

print(f"Acertou! Total de tentativas: {tentativas}")
