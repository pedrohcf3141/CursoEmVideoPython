#Desafio 91
from random import randint
from time   import sleep
# noinspection PyUnresolvedReferences

jogos = {}
lista = []
for x in range(1,5):
    jogos['Jogador'+ str(x)] = randint(1,6)
    print(f'O Jogador{x} tirou {jogos["Jogador" + str(x)]}')
    sleep(0.5)
print('Ranking dos jogadores')
for x in jogos.items():
    lista.append(x)
lista2 = []
lista2 = sorted(lista,key = lambda jogador: jogador[1], reverse=True)

for cont in range(0,4):
    print(f' {cont+1}o colocado foi o jogador {lista2[cont][0]} com {lista2[cont][1]}')
    sleep(0.5)