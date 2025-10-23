import customtkinter as ctk
import mysql.connector


conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",  
    database="quiz_uc7"
)
cursor = conexao.cursor(dictionary=True)


cursor.execute("SELECT * FROM perguntas")
perguntas = cursor.fetchall()


indice = 0
pontuacao = 0


def verificar(resposta):
    global indice, pontuacao
    if resposta == perguntas[indice]["resposta_correta"]:
        pontuacao += 1
    indice += 1
    if indice < len(perguntas):
        mostrar_pergunta()
    else:
        mostrar_resultado()


def mostrar_pergunta():
    questao = perguntas[indice]
    texto_questao.configure(text=questao["questao"])
    botao_a.configure(text="A) " + questao["alternativa_a"], command=lambda: verificar("A"))
    botao_b.configure(text="B) " + questao["alternativa_b"], command=lambda: verificar("B"))
    botao_c.configure(text="C) " + questao["alternativa_c"], command=lambda: verificar("C"))
    botao_a.pack(pady=5)
    botao_b.pack(pady=5)
    botao_c.pack(pady=5)
    botao_reiniciar.pack_forget()


def mostrar_resultado():
    texto_questao.configure(text=f"Fim do quiz! Pontuação: {pontuacao}/{len(perguntas)}")
    botao_a.pack_forget()
    botao_b.pack_forget()
    botao_c.pack_forget()
    botao_reiniciar.pack(pady=20)




def reiniciar_quiz():
    global indice, pontuacao
    indice = 0
    pontuacao = 0
    mostrar_pergunta()


ctk.set_appearance_mode("dark")
janela = ctk.CTk()
janela.title("Quiz de Manutenção de Software")
janela.geometry("500x300")


texto_questao = ctk.CTkLabel(janela, text="", font=("Arial", 16), wraplength=400)
texto_questao.pack(pady=20)


botao_a = ctk.CTkButton(janela, text="", width=400)
botao_a.pack(pady=5)


botao_b = ctk.CTkButton(janela, text="", width=400)
botao_b.pack(pady=5)


botao_c = ctk.CTkButton(janela, text="", width=400)
botao_c.pack(pady=5)
botao_reiniciar = ctk.CTkButton(janela, text="Reiniciar", width= 400, command=reiniciar_quiz)

mostrar_pergunta()


janela.mainloop()
