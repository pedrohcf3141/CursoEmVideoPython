# Desafio 28
import random
import time


nro = random.randint(0,5)
num = int(input('Digite um numero de 0 a 5 '))
print('Processando ...')
time.sleep(3.0)

print('Acertou' if nro == num else 'errou')
print('o numero era {}'.format(nro))

