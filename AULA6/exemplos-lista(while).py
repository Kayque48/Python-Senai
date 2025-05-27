nova = []

while True:
    try:
        num = int(input("Digite um número inteiro(0 para sair): "))
        if num == 0:
            break
        nova.append(num)
    except ValueError:
        print("HAaaa ocê errou, piá")
        
print(nova)