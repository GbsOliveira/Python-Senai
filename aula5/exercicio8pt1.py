for i in range(3):
    print(i)

for i in range(2, 7, 2):
    print(i)

contador = 5
while contador > 0:
    print(contador)
    contador -= 2

total = 0
for numero in range(1, 4):
    total += numero
print(total)

for letra in "PY":
    print(letra)

for numero in range(1, 6):
    if numero == 3:
        continue
    print(numero)

for numero in range(1, 6):
    if numero == 4:
        break
    print(numero)