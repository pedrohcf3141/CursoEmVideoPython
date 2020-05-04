# Desafio 50
soma = 0
for x in range(1, 7):

    print("Digite um numero {}" .format(x), end=' ')
    nro = int(input())
    if nro % 2 == 0:
        soma += nro
print(soma)

