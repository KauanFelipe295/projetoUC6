C1 = False
C2 = False
produtos = {}
Q = int(input("Insira de produtos que serão cadastrados: "))
for _ in range(1,Q+1):
    P = str(input(f"Insira o nome do °{_} produto: "))
    N = int(input(f"Insira a quantidade do produto {P}: "))
    produtos[P] = N
print("\nEstoque da loja:")
for pro, qua in produtos.items():
    print(f"- {pro}: {qua} unidades")
print("")

print("Produtos com estoque zerado:")
for key1, qua1 in produtos.items():
    if qua1 == 0:
        print(f"- {key1}")
        C1 = True
if C1 == True:
    print("\nNenhum Produto zerado")

print("Produtos com estoque acima de 500:")
for key2, qua2 in produtos.items():
    if qua2 >= 500:
        print(f"- {key2}")
        C2 = True
if C2 == True:
    print("\nNenhum Produto acima de 500")