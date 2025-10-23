import customtkinter as ctk

principal = ctk.CTk() #criando uma janela
ctk.set_appearance_mode("dark")
principal.iconbitmap("pikachu.ico")
principal.geometry("400x300")
principal.title("Pikachugame")


bnt = ctk.CTkButton(principal, text="Play")
bnt.pack(pady=30)

principal.resizable(width=False, height=False)
principal.mainloop()