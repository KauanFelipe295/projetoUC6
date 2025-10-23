M = 0.0
class Aluno:
    def __init__(self, nome, matricula, curso, nota1, nota2):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
    
    def calcular_media(self):
        media = (self.nota1 + self.nota2)/2
        return media
    
    def verificar_aprovacao():
        if Aluno.calcular_media >= 7.0:
            return "Aprovado"
        else:
            return "Reprovado"
        
    def exibir_dados(self):
        return f"Nome: {self.nome} || Matricula {self.matricula} || curso: {self.curso} || 1° Nota: {self.nota1:.2f} || 2° Nota: {self.nota2:.2f} || Média: {Aluno.calcular_mediar():.2f}"
    
no = str(input("Insira o nome do aluno: "))
ma = str(input("Insira a matricula do aluno: "))
cu = str(input("Insira o curso do aluno: "))