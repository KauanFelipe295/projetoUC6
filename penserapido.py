import customtkinter as ctk
import mysql.connector
import random
from PIL import Image



def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="pense_rapido"
    )





def clear_screen(app):
    for Widget in app.winfo_children():
        Widget.destroy()







def criar_menu(app):
    menu_frame = ctk.CTkFrame(app)
    menu_frame.pack(fill="both", expand=True)
    img = ctk.CTkImage(light_image=Image.open("penserapidopng.png"), size=(400, 200))
    ctk.CTkLabel(menu_frame, text="",image=img).pack(pady=0)
    bnt_cadastro = ctk.CTkButton(menu_frame, text="Cadastrar Perguntas", command=lambda:tela_categorias(app), width=200, height=40)
    bnt_cadastro.pack(pady=20)
    bnt_play = ctk.CTkButton(menu_frame, text="Iniciar Quiz", command=lambda: tela_quiz_placeholder(app), width=200, height=40)
    bnt_play.pack(pady=10)



def tela_quiz_placeholder(app):
    clear_screen(app)
    frame = ctk.CTk.Frame(app)
    frame.pack(fill="both", expand=True)
    label = ctk.CTkLabel(frame, text="Quiz em desenvolvimento! Volte ao menu para cadastrar perguntas.", font=("Arial", 16))
    label.pack(pady=50)
    bnt_voltar = ctk.CTkButton(frame, text="Voltar Menu", command=lambda: voltar_menu(app))
    bnt_voltar.pack(pady=20)



def tela_categorias(app):
    clear_screen(app)
    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)
    titulo = ctk.CTkLabel(frame, text="Escolha a Categoria para Cadastro", font=("Arial", 20, "bold"))
    titulo.pack(pady=30)
    categorias = ["Banco de Dados", "Português", "História", "Geografia", "Programação", "Manutenção de Software", "LGPD"]



    for cat in categorias:
        bnt_cat = ctk.CTkButton(frame, text=cat, command=lambda c=cat: tela_cadastro_pergunta(app, c), width=250, height=40)
        bnt_cat.pack(pady=10)
    bnt_voltar = ctk.CTkButton(frame, text="Voltar ao Menu", command=lambda: voltar_menu(app))
    bnt_voltar.pack(pady=20)

def tela_cadastro_pergunta(app, categoria):
    clear_screen(app)
    frame = ctk.CTkFrame(app)
    frame.pack(fill="both", expand=True)

    titulo = ctk.CTkLabel(frame, text="Perguntas:", font=("Arial", 14, "bold"))
    titulo.pack(pady=10)

    lbl_pergunta = ctk.CTkLabel(frame, text="Pergunta:", font=("Arial, 14," "bold"))
    lbl_pergunta.pack(pady=5)
    pergunta_entry = ctk.CTkEntry(frame, placeholder_text="Digite a pergunta", height=40, width=550)
    pergunta_entry.pack(pady=5)

    lbl_resposta = ctk.CTkLabel(frame, text="Resposta Correta:", font=("Arial", 14, "bold"))
    lbl_resposta.pack(pady=(20, 3))
    resposta_entry = ctk.CTkEntry(frame, placeholder_text="Diigite a resposta correta (texto livre)", height=40, width=550)
    resposta_entry.pack(pady=5)

        
    def salvar():
        pergunta = pergunta_entry.get().strip()
        resposta = resposta_entry.get().strip() 

        if not pergunta or not resposta:
            aviso = ctk.CTkLabel(frame, text="Preencha a pergunta e a resposta corretamente", text_color="red", font=("Arial", 12))
            aviso.pack(pady=20)
            return
        
        try:
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO perguntas(pergunta, categoria, resposta)"
                "VALUES (%,%,%)"
                (pergunta, categoria, resposta)
            )
            conn.comit()
            conn.close()

            sucesso = ctk.CTkLabel(frame, text="Pergunta cadastrada com sucesso", text_color="green", font=("Arial", 14 , "bold"))
            sucesso.pack(pady=20)

            pergunta_entry.delete(0, "end")
            resposta_entry.delete(0, "end")
        
        except mysql.connector.Error as err:
            erro = ctk.CTkLabel(frame, text=f"Errro no banco: {str(err)}", text_color="red", font=("Arial", 12))
            erro.pack(pady=10)

    bnt_salvar = ctk.CTkButton(frame, text=f"Cadastrar", command=salvar, width=150, height=40)
    bnt_salvar.pack(pady=20)

    def continuar():
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkLabel) and ("sucesso" is str(widget.cget("text")) or "Erro" in str(widget.cget("text")) or "Preencha" in str(widget.cget("text"))):
                widget.destroy()

        pergunta_entry.delete(0, "end")
        resposta_entry.delete(0, "end")

    bnt_continuar = ctk.CTkButton(frame, text="Continuar Cadastrando", command=continuar, width=200, height=40)
    bnt_continuar.pack(pady=5)

    bnt_voltar = ctk.CTkButton(frame, text="Voltar ao Menu", command=lambda: voltar_menu(app), width=150, height=40)
    bnt_voltar.pack(pady=10)


def voltar_menu(app):
    clear_screen(app)
    criar_menu(app)







if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.geometry("500x500")
    app.title("Pense Rápido")
    criar_menu(app)
    app.mainloop()

    app.rowconfigure(0, weight= 1)
    app.columnconfigure(0, weight= 1)

    















    