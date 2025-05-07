idade = int(input("Digite sua idade: "))

if idade == 5 or idade <= 7:
    print(f"idade = {idade}! Nadador infantil A.")
elif idade == 8 or idade <= 11:
    print(f"idade = {idade}! Nadador infantil B.")
elif idade == 12 or idade == 13:
    print(f"idade = {idade}! Nadador juvenil A.")
elif idade == 14 or idade <=17:
    print(f"idade = {idade}! Nadador juvenil B.")
elif idade >= 18:
    print(f"idade = {idade}! Nadador adulto.")
else:
    print(f"idade = {idade}! Nadador com menos da idade minima.")