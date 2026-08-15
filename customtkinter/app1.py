import customtkinter as ctk

ctk.set_appearance_mode("dark")

#Criar a janela principal do app
janela = ctk.CTk()

#Definir um tamanho para a janela
janela.geometry("400x300")

#Criar um texto para incluir na janela
texto = ctk.CTkLabel(janela, text="---Ola!!---")
texto1 = ctk.CTkLabel(janela, text="---Senai---")


#Incluir o texto na janela
texto.pack(pady=100)
texto1.pack()

janela.mainloop()