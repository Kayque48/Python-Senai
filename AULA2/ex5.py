valor = float(input("Insira o valor: "))
taxa = float(input("Insira o valor da taxa: "))
tempo = float(input("Insira o tempo utilizado: "))

prestacao = valor + (valor * (taxa/100) * tempo)

print(f"A prestação é {prestacao}")