# Desafio 35

nro1 = int(input('numero 1 '))
nro2 = int(input('numero 2 '))
nro3 = int(input('numero 3 '))

if ((nro3 + nro2) < nro1) or ((nro2 + nro1) < nro3) or ((nro3 + nro1) < nro2):
    print('NÃO É POSSIVEL ISSO SER UM TRIANGULO')
else:
    print('É POSSIVEL ISSO SER UM TRIANGULO')



