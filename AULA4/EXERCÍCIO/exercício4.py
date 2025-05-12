pessoas = int(input("Insira a quantidade de pessoas no grupo: "))

soma = 0
soma_M = 0
soma_F = 0

qntde = 0
qntde_M = 0
qntde_F = 0

media = 0
media_M = 0
media_F = 0


for pessoa  in range(pessoas):
    idade = int(input("Insira sua idade:"))
    sexo = input("Insira seu sexo(M/F): ")
    
    soma += idade
    qntde += 1
    
    
    if sexo == "M" or sexo == "m":
        soma_M += idade
        qntde_M += 1
    
    elif sexo == "F" or sexo == "f":
        soma_F += idade
        qntde_F += 1
        
    else:
        print("Valor de sexo inválido.")
        
media = soma / qntde
        
if qntde_F == 0:        
    media_M = soma_M / qntde_M
    
    print(f"A média masculina é: {media_M}")
    print(f"Não há mulheres no grupo.")
    print(f"A média de todo o grupo é: {media}")
    
else:
    media_F = soma_F / qntde_F
    print(f"Não há homens no grupo.")
    print(f"A média Feminia é: {media_F}")
    print(f"A média de todo o grupo é: {media}")
