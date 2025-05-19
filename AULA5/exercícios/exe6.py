palavra = []

letra = iter(lambda: input("Digite uma palavra (ou pressione Enter para finalizar): "), "")


while letra != "":
    palavra.append(letra)

invertido = list(reversed(palavra))

print(invertido)
