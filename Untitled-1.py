import mysql.connector
import tkinter as tk 
from tkinter import Toplevel
from datetime import datetime, timedelta
from tkinter import Toplevel, messagebox, Listbox

bd = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "biblioteca"
)

cursor = bd.cursor()

def cadastrar_usuario():
    print("Não ta pronto")

#Tela cadastro de Usuario


def tela_cadastro():
    janela = Toplevel()
    janela.title("Cadastro de usuario")
    janela.geometry("600x500")
    tk.Label(janela, text="Cadastro de Usuario", pont=("Arial",12).pack(pady=20))
    tk.Label(janela, text="Nome").pack()
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()
    tk.Label(janela, text="Email").pack()
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()



janela = tk.Tk()
janela.geometry("600x500")
janela.title("Gerenciamanto de Emprestimos")
tk.Label(janela, text="Bem vindo a Biblioteca", font=("Arial", 14, "bold"), fg="blue").pack(pady=20)
tk.Button(janela, text="Cadastrar usuário",)



def tela_cadastro_livros():
    janela = Toplevel()
    janela.title("Cadstro de Usuários")
    janela.geometry("600x500")
    tk.Label(janela, text = "Cadastro de usuario", font=("arial", 12).pack(pady=20))
    tk.Label(janela, text="Nome").pack()
    entrada_nome = tk.Entry(janela)
    entrada_nome.pack()
    tk.Label(janela, text="email").pack()
    entrada_email = tk.Entry(janela)
    entrada_email.pack()
    
    tk.Button(janela, text="Cadastrar", command= lambda: cadastrar_usuario(entrada_nome.get(), entrada_email.get(), janela).pack(pady=20))

cursor = bd.cursor()
janela = tk.Tk()
janela.geometry("600x500")




def emprestar_livro(id_livro, id_usuario, janela):
    hoje = datetime.today().date()
    devolucao = hoje + timedelta(days = 7)
    cursor.execute("select disponivel from livros Where id= %s", (id_livro))
    resultado = cursor.fetchone()
    if resultado and resultado[0]:
        cursor.execute("Insert into emprestimos (id_livro, id_usuario, data_emprestimo, data_devolucao) values (%,%,%,%)", (id_livro, id_usuario, hoje, devolucao))
        cursor.execute("Update livros Set disponivel = false where id= %", (id_livro))
        bd.commit()
        messagebox.showerror("Sucesso", "Livro emprestado", parent = janela)
    else:
        messagebox.showerror("Erro", "Livro indiponivel", parent=janela)




def tela_consulta():
    janela = Toplevel()
    janela.title("Consulta de Livros Disponíveis")
    janela.geometry("400x300")

    lista = Listbox(janela, width=50)
    lista.pack(pady=10)

    cursor.execute("SELECT id,titulo, autor FROM livros WHERE disponivel = TRUE")
    for l in cursor.fetchall():
        lista.insert(tk.END, f"{l[0]} - {l[1]} - ({l[2]})")




janela.mainloop()