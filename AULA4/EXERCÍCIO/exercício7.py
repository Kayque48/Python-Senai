numb = int(input("Insira o número que deseja saber o fatorial: "))

fatorial = 1

for i in range(numb, 0,-1):
    fatorial *= i

print(fatorial)


