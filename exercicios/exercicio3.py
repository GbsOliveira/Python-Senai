#Area e perimetro

def medidas (b, a):
    area = b * a
    perimetro = 2 * (b + a)
    return area, perimetro

#print (medidas(20, 20))
base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))

area, perimetro = medidas(base, altura)
print(f"Área: {area:.2f}, \nPerímetro: {perimetro:.2f}")
