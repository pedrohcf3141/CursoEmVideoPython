# Desafio 34

salario = float(input('Salario '))

if salario <= 1250.0:
    print('aumento de R$ {} '.format(salario * 0.15))
else:
    print('aumento de R$ {} '.format(salario * 0.10))


