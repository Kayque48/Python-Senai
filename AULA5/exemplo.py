notas = 0
qnt_notas_info = 0
while True:
    nota = float(input("Informe a nota (-1 para finalizar): "))
    if(nota == -1):
        break
    notas = notas + nota
    qnt_notas_info = qnt_notas_info + 1
    if qnt_notas_info > 0:
        media = notas/qnt_notas_info
        print(f"Quantidade de nota informadas: {qnt_notas_info}")
        print(f"Média: {media:.2f}")
    else:
        print("Nenhuma nota informada.")