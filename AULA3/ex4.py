numb1 = float(input("Insira o valor do primeiro número: "))
numb2 = float(input("Insira o valor do segundo número: "))

print("Insira os valores das quatro operações:")

resultado_soma = float(input("Insira o valor da soma: "))
resultado_sub = float(input("Insira o valor da subtração: "))
resultado_mul = float(input("Insira o valor da multiplicação: "))
resultado_div = float(input("Insira o valor da divisão: "))

if resultado_soma == numb1 + numb2:
    print("Resultando correto!")
else:
    print("Resultado incorreto!")
if resultado_sub == numb1 - numb2:
    print("Resultando correto!")
else:
    print("Resultado incorreto!")
if resultado_mul == numb1 * numb2:
    print("Resultando correto!")
else:
    print("Resultado incorreto!")
if resultado_div == numb1 / numb2:
    print("Resultando correto!")
else:
    print("Resultado incorreto!")