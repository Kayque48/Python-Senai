while True:
    resposta = input("Você gosta de Python?(sim/não) ")
    ress = resposta.upper()

    if ress != "SIM":
        print("Esta não é a resposta correta")
    else:
        print("Resposta correta!")