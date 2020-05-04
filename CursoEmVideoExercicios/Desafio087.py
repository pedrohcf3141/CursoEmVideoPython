#Desafio 87
matrix = []
soma = par = 0
for item in range(0,3):
    lista = []
    for nro in range(0,3):
        num = int(input(f"Digite o item na posição[{item},{nro}]: "))
        lista.append(num)
        if num % 2 == 0:
            par += num
        if lista.index(num) == 2:
            soma +=num
    matrix.append(lista[:])
    lista.clear()
print(30*"=-")
for item in matrix:
    print(item)
print(30*"=-")
print(f" a soma dos numeros pares é {par}")
print(30*"=-")
print(f" a soma dos numeros da terceira coluna é {soma}")
print(30*"=-")
print(f"o maior numero da segunda linha é {max(matrix[1])}")

