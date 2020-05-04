# Desafio 59

from time import sleep

nro1 = int(input("Digite o primeiro numero "))
nro2 = int(input("Digite o segundo numero "))
maior = 0
menu = ""

while menu != '5':
    menu = input('''
                 [1]
    SOMAR
    [2]
    MULTIPLICAR
    [3]
    MAIOR
    [4]
    NOVOS
    NUMEROS
    [5]
    SAIR
    DO
    PROGRAMA
    ''').strip()

    if menu == '1':
        print('a soma é {}'.format(nro1 + nro2))
        continue
    elif menu == '2':
        print('a multiplicação é {}'.format(nro1 * nro2))
        continue
    elif menu == '3':
        if nro1 >= nro2:
            maior = nro1
        else:
            maior = nro2
        print(' o maior numero é {}'.format(maior))
        continue
    elif menu == '4':
        nro1 = int(input("Digite o primeiro numero "))
        nro2 = int(input("Digite o segundo numero "))
        continue
    elif menu == '5':
        print('saindo ', end='')

        sleep(1)

    else:
        print('opção invalida')
        continue
print('fim')


