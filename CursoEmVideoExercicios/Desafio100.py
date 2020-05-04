def sorteia ():
    from random import randint
    from time   import sleep
    print('Sorteando 5 valores da lista', end=' ')
    lista  = list()
    for nro in range(0,5):
        lista.append(randint(0,10))
        print(lista[nro],end=' ')
        sleep(0.5)
    print('PRONTO')
    return lista

def somaPar (nro):
    sp = 0
    for x in range(0, len(nro)):
        if int(nro[x]) % 2 == 0:
            sp += int(nro[x])
    print(f'Somando os valores pares de {nro}, temos {sp}')


somaPar(sorteia())
