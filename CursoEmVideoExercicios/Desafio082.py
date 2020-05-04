#Desafio 82
lista =[]
par =[]
impar = []
while True:
    nro = int(input('Digite um número: '))
    lista.append(nro)
    if nro % 2 == 0 :
        par.append(nro)
    else:
        impar.append(nro)
    resposta = input('Quer continuar [S/N]')
    if resposta in 'Nn':
        break
print(f'A lista completa é {lista}')
print(f'Os númreos pares digitados são {par}')
print(f'Os números impares digitados são {impar}')

