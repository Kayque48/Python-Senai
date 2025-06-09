P1 = (6, 7, 1, 6, 4,)
P2 = (8, 10, 9, 5, 7)

soma1 = 0
qnt1 = 0

for nota1 in P1:
    soma1 += nota1
    qnt1 += 1
    
media1 = soma1 / qnt1
print(f"Média da P1: {media1}") 

soma2 = 0
qnt2 = 0

for nota2 in P2:
    soma2 += nota2
    qnt2 += 1
    
media2 = soma2 / qnt2
print(f"Média da P2: {media2}")

if(media1 > media2):
    print("A melhor média foi na Prova1!")
elif(media2 > media1):
    print("A melhor média foi na Prova 2!")
else:
    print("As médias das duas provas foi iguais!")