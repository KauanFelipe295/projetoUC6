import customtkinter as ctk
from PIL import Image


imagem = Image.open("logo-SENAC.png")

imagem.show()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def mostrartela(tela):
    tela.tkraise()

janela = ctk.CTk()
janela.geometry("500x500")
janela.title("Jogos Internos Mediotec")

janela.rowconfigure(0, weight=1)
janela.columnconfigure(0, weight=1)

telabemvindo = ctk.CTkFrame(janela)
telacadastro = ctk.CTkFrame(janela)
telalogin = ctk.CTkFrame(janela)

for tela in (telabemvindo, telacadastro, telalogin):
    tela.grid(row=0, column=0, sticky="nsew")  


ctk.CTkLabel(telabemvindo, text="Jogos Internos Mediotec", font=("Arial", 28, "bold")).pack(pady=40)
ctk.CTkButton(telabemvindo, text="Cadastro", command=lambda: mostrartela(telacadastro)).pack(pady=10)
ctk.CTkButton(telabemvindo, text="Login", command=lambda: mostrartela(telalogin)).pack(pady=10)

ctk.CTkLabel(telacadastro, text="Você está na Tela de Cadastro", font=("Arial", 16)).pack(pady=20, expand=True)
ctk.CTkButton(telacadastro, text="Voltar ao Menu", command=lambda: mostrartela(telabemvindo)).pack(pady=10)


ctk.CTkLabel(telalogin, text="Você está na Tela de Login", font=("Arial", 16)).pack(pady=20, expand=True)
ctk.CTkButton(telalogin, text="Voltar ao Menu", command=lambda: mostrartela(telabemvindo)).pack(pady=10)


mostrartela(telabemvindo)
janela.mainloop()