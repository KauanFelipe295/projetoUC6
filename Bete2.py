import customtkinter as ctk
def butao():
    print("botão pressionado")

ctk.set_appearance_mode("dark") #light para tema claro
root = ctk.CTk()
root.geomtry("400x300")
root.title("Exemplo CustomTkinter")
#Criar um botão customizado
botao = ctk.CTkButton(root, text="CLique aqui", command=butao)
botao.pack(pady=20)

root.iconbitmap("corda.ico")
#Incia o loop da interface
root.mainloop()