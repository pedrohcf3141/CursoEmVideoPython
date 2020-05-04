# Desafio 33

nro1 = int(input('numero 1 '))
nro2 = int(input('numero 2 '))
nro3 = int(input('numero 3 '))

lista = []

lista.append(nro1)
lista.append(nro2)
lista.append(nro3)
lista.sort()
print('MAIOR {}'.format(lista[-1]))
print('MENOR {}'.format(lista[0]))

print()

if nro1 >= nro2 and nro1 >= nro3:
    print('MAIOR {}'.format(nro1))
elif nro2 >= nro1 and nro2 >= nro3:
    print("MAIOR {}".format(nro2))
else:
    print('MAIOR {}'.format(nro3))

if nro1 <= nro2 and nro1 <= nro3:
    print('MENOR {}'.format(nro1))
elif nro2 <= nro1 and nro2 <= nro3:
    print("MENOR {}".format(nro2))
else:
    print('MENOR {}'.format(nro3))



