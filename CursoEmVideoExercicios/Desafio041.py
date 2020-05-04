#Desafio 41

from datetime import date

ano = int(input('ano do nascimento '))
idade = date.today().year - ano


if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')


