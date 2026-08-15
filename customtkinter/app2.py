import customtkinter as ctk

#Funções
def acao():
    resposta.configure(text="Clicou")

ctk.set_appearance_mode("system")

tela = ctk.CTk() 
tela.geometry("400x200")
tela.title("Teste de botão")

#Criar e inserir um título na tela
titulo = ctk.CTkLabel(tela, text="APP PARA TESTE DE BOTAO", font=("Arial", 22))
titulo.pack(pady = 20)

botao = ctk.CTkButton(tela, text="CLIQUE AQUI", command = acao)
botao.pack(pady = 20)

resposta = ctk.CTkLabel(tela, text="")
resposta.pack(pady = 20)

tela.mainloop()
