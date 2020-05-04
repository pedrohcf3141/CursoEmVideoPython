# Desafio 76

tupla = ('pao',2.00,'hamburguer',1.00,'queijo',2.50,'molho',4.50)

for x in tupla:
    if tupla.index(x) % 2 ==0:
        print(x,end=" R$: ")
        print(tupla[tupla.index(x)+1])
#Solução Guanabara
for pos in range(0,len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<15}',end="R$: ")
    else:
        print(f'{tupla[pos]:>5.2f}')

