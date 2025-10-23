R = 0
N = int(input("Insira um numero inteiro: "))
for NU in range(1,N+1,2):
    R += NU
print(f"A soma dos ímpares de 1 a {N} é {R}.")