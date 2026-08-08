"""
Crie um programa que:

1. Receba três medidas de lados (`float`).
2. Verifique com operadores lógicos se elas formam
 um triângulo: cada lado deve ser menor que a soma 
 dos outros dois.
3. Se formar, classifique em **equilátero**, 
**isósceles** ou **escaleno**.

"""
#triangulo equilatero = a+b+c
#triangulo isosceles = 2lados iguais e 1 nao
#triangulo escaleno = a1!=b!=c

a = float(input(f"Informe a primeira medida: "))
b = float(input(f"Informe a segunda medida: "))
c = float(input(f"Informe a terceira medida: "))

if a==b==c:
    print(f"triangulo equilatero")
elif a==b or b==c and b==a or c==a:
    print(f"triangulo isosceles")
elif a!=b!=c:
    print(f"triangulo escaleno")
