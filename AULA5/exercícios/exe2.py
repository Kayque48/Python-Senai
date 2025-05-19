maior = 0
qnt = 0
soma = 0
menor = 9999999999999999999999

numb = 1

while numb < 11:
    valor = int(input(f"Insira {numb} valores inteiros: "))
    
    if maior < valor:
        maior = valor

        
        
    if menor > valor:
        menor = valor
        
    soma += valor
    qnt += 1
    
    numb += 1
    
media = soma / qnt
    
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")
print(f"A média é {media}")
        
    
