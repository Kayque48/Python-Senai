# Cria uma lista com nomes de carros
tupla_carros = "Gol", "Corolla", "Civic", "Opala", \
"Tucson", "Elantra"
carro1, *carros = tupla_carros
print(f"Carro1: {carro1}")
print(f"Carros: {carros}")