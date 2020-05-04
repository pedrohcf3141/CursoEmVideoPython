# Desafio 40

nota1 = float(input(' nota 1 '))
nota2 = float(input(' nota 2 '))
media = (nota2 + nota1) / 2

if media < 5:
    print('REPROVADO')
elif media < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')



