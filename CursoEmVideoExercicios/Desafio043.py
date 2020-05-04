# DESAFIO 43

altura = float(input('altura '))
peso = float(input('peso '))
imc = peso / pow(altura,2)


if peso < 18.5:
    print('ABAIXO DO PESO')
elif peso< 25:
    print('PESO IDEAL')
elif peso < 30:
    print('SOBRE PESO')
elif peso < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')



