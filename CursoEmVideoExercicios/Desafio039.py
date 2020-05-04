# desafio 39

from datetime import date

ano = int(input('ano do nascimento '))
idade = date.today().year - ano


if idade == 17:
    print('esse é seu ano de alistamento')
elif idade < 17:

    print('seu ano de alistamento será em {}'.format(ano + 17))
else:
    print('seu ano de alistamento foi em {}'.format(ano + 17))


