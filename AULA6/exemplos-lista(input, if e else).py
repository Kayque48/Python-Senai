letras = ["a", "b", "c", "d", "e", "f"]
var = input("informe uma letra: ")
if var.lower() in letras:
    print(f"A Letra '{var.lower()}' está na lista")
else:
    print(f"A Letra '{var.lower()}' NÃO está na lista")