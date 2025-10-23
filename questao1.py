T1 = int(input("Insira o  primeiro lado do triangulo: "))
T2 = int(input("Insira o  segundo lado do triangulo: "))
T3 = int(input("Insira o  terceiro lado do triangulo: "))
if T1 != 0 and T2 != 0 and T3 != 0:
    if T1+T2 > T3 or T1+T3 > T2 or T2+T3 > T1:
        if T1 == T2 and T2 == T3:
            print("Triangulo Equilátero.")
        elif T1 == T2 or T2 == T3 or T1 == T3:
            print("Triangulo Isósceles.")
        else:
            print("Triangulo Escaleno.")
    else:
        print("Não forma um triangulo.")
else:
    print("Não forma um triangulo.")