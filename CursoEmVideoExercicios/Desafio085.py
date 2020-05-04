#Desafio 85
lista = [[],[]]

for num in range(1,8):
    nro = int(input(f"Digite {num}o numero para a lista "))
    if nro % 2 == 0:
        lista[0].append(nro)
        lista[0].sort()
    else:
        lista[1].append(nro)
        lista[1].sort()
print(30*"=-")
print(f"Os numeros pares digitados são {lista[0]}")
print(f"Os numeros impares digitados são {lista[1]}")

