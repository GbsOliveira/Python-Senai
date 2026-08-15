import customtkinter as ctk

def somar():
    a=float(primnum.get())
    b=float(segnum.get())
    #Somar os valores
    soma=a+b
    #Atualizar o texto do resultado
    resultado.configure(text=f"Resultado: {soma:.2f}")
    print(soma)

def subtrair():
    a=float(primnum.get())
    b=float(segnum.get())
    sub=a-b
    resultado.configure(text=f"Resultado: {sub:.2f}")
    print(sub)

def multiplicar():
    a=float(primnum.get())
    b=float(segnum.get())
    mult=a*b
    resultado.configure(text=f"Resultado: {mult:.2f}")
    print(mult)

def dividir():
    a=float(primnum.get())
    b=float(segnum.get())
    div=a/b
    resultado.configure(text=f"Resultado: {div:.2f}")
    print(div)

ctk.set_appearance_mode("system")

janela = ctk.CTk()
janela.geometry("300x400")

titulo_app = ctk.CTkLabel(janela, text="Calculadora", font=("ARIAL", 18))
titulo_app.pack(pady = 20)

primnum = ctk.CTkEntry(janela, placeholder_text="Primeiro número")
segnum = ctk.CTkEntry(janela, placeholder_text="Segundo número")

primnum.pack(pady=10)
segnum.pack(pady=10)

botao1 = ctk.CTkButton(janela, text="Soma", command=somar)
botao1.pack(pady=5)

botao2 = ctk.CTkButton(janela, text="Substrair", command=subtrair)
botao2.pack(pady=5)

botao3 = ctk.CTkButton(janela, text="Multiplicar", command=multiplicar)
botao3.pack(pady=5)

botao4 = ctk.CTkButton(janela, text="Dividir", command=dividir)
botao4.pack(pady=5)

#Saída
resultado = ctk.CTkButton(janela, text="Resultado: ", fg_color="yellow", text_color="black")
resultado.pack(pady=5)


janela.mainloop()