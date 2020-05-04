#Desafio 58

from random import randint

aleatorio = randint(0,100)
nro = int(input("Digite umnumero de 0 ate 100 "))
cont = 1
while nro != aleatorio:
    print('numero incorreto ',end = " ")
    if nro < aleatorio:
        nro = int(input("Tente um numero maior "))
    else:
        nro = int(input("Tente um numero menor "))
    cont +=1
print('fim com {} tentativas'.format(cont))



