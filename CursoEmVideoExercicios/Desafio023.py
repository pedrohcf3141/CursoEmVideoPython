# Desafio 23

nro = input('Informe um numero ')
nro = '0000'+nro

print(' o numero tem {} Unidades '.format(nro[-1]))
print(' o numero tem {} Dezenas'.format(nro[-2]))
print(' o numero tem {} Centenas '.format(nro[-3]))
print(' o numero tem {} Milhares '.format(nro[-4]))

nro = int(nro)

print('Unidades {}'.format(nro%10))
print('Dezenas {}'.format(((nro//10)%10)))
print('Centenas {}'.format(((nro//100)%10)))
print('Milhares {}'.format(((nro//1000)%10)))
