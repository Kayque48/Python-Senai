palavra = []

for letra in iter(lambda: input("Digite uma palavra (ou pressione Enter para finalizar): "), ""):
    palavra.append(letra)

invertido = list(reversed(palavra))

print(invertido)
