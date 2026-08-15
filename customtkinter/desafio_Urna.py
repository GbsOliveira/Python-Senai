import customtkinter as ctk

votos_candidato1 = 0
votos_candidato2 = 0

#FUNÇÕES
def votar_candidato1():
    global votos_candidato1
    votos_candidato1 += 1
    print(votos_candidato1)

def votar_candidato2():
    global votos_candidato2
    votos_candidato2 += 1
    print(votos_candidato2)

def apurar_resultado():
    global votos_candidato1
    global votos_candidato2

    if votos_candidato1 > votos_candidato2:
        texto_resultado.configure(text = "CANDIDATO 1 VENCEU")
    elif votos_candidato2 > votos_candidato1:
        texto_resultado.configure(text = "CANDIDATO 2 VENCEU")
    else:
        texto_resultado.configure(text = "EMPATE")

    print()


ctk.set_appearance_mode("system")

janela = ctk.CTk()
janela.geometry("300x600")

titulo_app = ctk.CTkLabel(janela, text="VOTAÇÃO DE REPRESENTANTE", font=("ARIAL", 18))
titulo_app.pack(pady = 20)

texto_candidato1 = ctk.CTkLabel(janela, text = "CANDIDATO 1 - Joãozinho")
texto_candidato2 = ctk.CTkLabel(janela, text = "CANDIDATO 2 - Luquinha")

texto_candidato1.pack(pady = 10)
texto_candidato2.pack(pady = 10)

botao_candidato1 = ctk.CTkButton(janela, text="Candidato 01", command = votar_candidato1)
botao_candidato1.pack(pady = 5)
botao_candidato2 = ctk.CTkButton(janela, text="Candidato 02", command = votar_candidato2)
botao_candidato2.pack(pady = 5)

botao_resultado = ctk.CTkButton(janela, text = "RESULTADO", fg_color = "red", command = apurar_resultado)
botao_resultado.pack(pady = 10)

texto_resultado = ctk.CTkLabel(janela, text = "")
texto_resultado.pack(pady = 10)

janela.mainloop()