numeros = [1]

for numero in numeros:
    nome = input("Cadastre seu nome de usuário: ")
    senha = input("Cadastre sua senha: ")
    if nome == senha:
        print("ERRO!\nA senha e o nome de usuário não podem ser iguais.\n\n")
        numeros.append(numeros)
    else:
        print("Cadastro feito com sucesso.")
    
      
    