time1 = int(input("Digite a quantidade de pontos do time 1: "))
time2 = int(input("Digite a quantidade de pontos do time 2: "))

if time1 > time2:
    print(f"O time 1 levou a vitória com {time1} pontos!")
elif time1 < time2:
    print(f"O time 2 levou a vitória com {time2} pontos!")
else:
    print(f"Empate, ambos os times fizeram {time1} pontos!")
            