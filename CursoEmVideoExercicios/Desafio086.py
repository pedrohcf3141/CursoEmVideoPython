#Desafio 86
matrix = []
for item in range(0,3):
    lista = []
    for nro in range(0,3):
        num = int(input(f"Digite o item na posição[{item},{nro}]: "))
        lista.append(num)
    matrix.append(lista[:])
    lista.clear()
for item in matrix:
    print(f"{item}")

