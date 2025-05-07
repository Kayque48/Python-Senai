maior =  0
soma = 0
quantidade = 0

for numero in [10,54,12,75,12,86,12,97,3,89]:
    
    soma += numero

    print(f"Numeros: {numero}")
    if maior <= numero:
        maior = numero
        
        menor = maior
        
    if menor >= numero:
        menor = numero
    quantidade += 1 

    
media = soma / quantidade
print(quantidade)
print(f"Maior: {maior}")
print(f"Menor: {menor}")    
print(f"Média: {media}")