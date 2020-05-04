#Desafio 32

from datetime import date
ano =int(input('Digite o ano para ser analizado ou 0 para o atual '))


if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bissexto')
else:
    print('ano não é bissexto')

print('fim')



