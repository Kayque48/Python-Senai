pessoas = int(input("Digite a quantidade de pessoas que fizeram o Exame: "))
soma = 0
quantidade = 0
x = 0
while x <= pessoas:
    print(f"\nResultado do Paciente {x+1}:")
    temperatura = float(input("Digite a temperatura do Paciente: "))
    if temperatura < 37.2:
        print("Paciente em estado normal.\n")
    elif temperatura <= 37.3:
        print("Paciente está em estado febril.\n")
    elif temperatura <= 39:
        print("Paciente está com febre.\n")
    else:
        print("Paciente com febre alta.\n")

    soma += temperatura
    quantidade += 1
    x += 1
    
media = soma / quantidade
print(f"A média das temperaturas é: {media}")