#Desafio 88
from random import randint
lista = []
palpite = []
nro = int(input("Quantos jogos você  que eu sorteie? "))
for jogos in range(0,nro):
        while len(palpite) <= 6:
            num = randint(0,60)
            if num not in palpite:
                palpite.append(num)
        palpite.sort()
        lista.append(palpite[:])
        palpite.clear()
for dica in lista:
    print(dica)
