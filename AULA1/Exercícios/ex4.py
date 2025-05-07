anoNascimento = int(input("Insira seu ano de nascimento: "))
idade = 2025 - anoNascimento

if anoNascimento < 2011:
    print(f"você tem {idade}. De maior")
else: print(f"você tem {idade}. De menor")
