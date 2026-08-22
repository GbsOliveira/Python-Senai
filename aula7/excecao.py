
try:
    a = int(input("Primeiro numero: "))
    b = int(input("Segundo numero: "))

    resultado = a/b
    print(f"{a} / {b} = {resultado}")
except ZeroDivisionError:
    print("Valor inválido - Não é possivel dividor por 0")
except NameError:
    print("Resultado não existe")
except ValueError:
    print("Digite um valor válido")
finally:
    print("Final do programa!!")

