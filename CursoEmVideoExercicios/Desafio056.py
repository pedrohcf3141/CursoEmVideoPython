#Desafio 56

idade = 0
velho = ''
soma = 0
contador = 0
sexo = 'f'
for x in range(1, 5):
    print('nome, idade ,sexo da pessoa {} separado por virgula'. format(x), end=" ")
    pessoa = input().split(',')
    soma += int(pessoa[1].replace(' ', ''))
    if idade <= int(pessoa[1].replace(' ', '')):
        velho = pessoa[0]
    if pessoa[2][0].lower() == sexo:
        contador += 1
print(' A média das idades é de {}\nO mais velho é o {}\n Temos {} Mulheres no Grupo'.format(soma / 4, velho, contador))


