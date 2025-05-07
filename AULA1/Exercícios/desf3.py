salario = float(input("Insira o salário: "))
aumento = float(input("Insira o aumento porcentual: "))

salario_aumento = float(salario / (aumento/100))
print(f"O salário atual: {salario_aumento:.2f}")