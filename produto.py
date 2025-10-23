class Produto:
    def __init__(self, nome, codigo, preco, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco = preco
        self.quantidade = quantidade

    def calcular(self):
        total = self.preco * self.quantidade
        return total
    
    def verificar_disp(self):
        if self.quantidade > 0:
            return "Disponivel"
        else:
            return "Indisponivel"
        
    def exibir_dados(self):
        total = self.calcular()
        disp = self.verificar_disp()
        print("\nDados de Estoque\n")
        print(f"Nome: {self.nome}")
        print(f"Código: {self.codigo}")
        print(f"Preço: R${self.preco:.2f}")
        print(f"Quantidade: {self.quantidade}")
        print(f"Valor Total: R${total:.2f}")
        print(f"Disponibilidade: {disp}")
    
def main():
    print("\nCadastro de produto\n")
    nome = input("Nome: ")
    codigo = (input("Código: "))
    preco = float(input("Preço: "))
    qnt = int(input("Quantidade: "))
    prod1 = Produto(nome, codigo, preco, qnt)
    prod1.exibir_dados()

main()