#Desafio 51

nro = int(input('numero '))
razao = int(input('razão '))
decimo = nro + (10-1) * razao
for x in range(nro,decimo + razao,razao):
    print('{}'.format(x),end="->")
print('Acabou')

