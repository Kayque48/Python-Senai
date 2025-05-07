valor_compra = float(input("Insira o valor da compra: "))
numero_prestacao = float(input("Insira o número das prestações:"))

valor_prestacao = valor_compra / numero_prestacao

if valor_prestacao != 0:
    print(f"O valor das prestações sem juros é {valor_prestacao:.2f}")
else:
    print(f"Valor invalido")
