N = 0
Usersoma = 0.0
semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
list = []
for T in semana:
    User = float(input(f"Informe a temperatura média de {T}: "))
    list.append(User)
    Usersoma += User
TM = Usersoma/7
print(f"Temperatura média semanal: {TM:.2f}C°")
print("Dias com temperatura acima da média:")
for _ in list:
    if _ > TM:
        print(f"{semana[N]} ({_:.2f}°C)")
        N += 1