# Lista 'compra' contém três números e uma lista de produtos como quarto elemento
compra = [10.2, 3.35, 16.3, ["tomate", "sabonete", "arroz"]]
print(compra)  # Exibe toda a lista 'compra'

# Acessa o quarto elemento da lista 'compra', que é outra lista
produtos = compra[3]
print(produtos)  # Exibe a lista de produtos

# Soma os três primeiros elementos da lista 'compra'
total = compra[0] + compra[1] + compra[2]
print(total)  # Exibe o total da soma

# Cria duas listas separadas: uma de letras e outra de números
letra = ["a", "b", "c"]
num = [2, 4, 6]

# Junta as duas listas em uma lista maior (lista de listas)
tudo = [letra, num]
print(tudo)  # Exibe a lista de listas

# Exibe apenas a lista de letras
print(f"Letras: {tudo[0]}")

# Exibe apenas a lista de números
print(f"Numeros: {tudo[1]}")