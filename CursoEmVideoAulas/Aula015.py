# aula de break

'''
n = s = 0
while True:
    n = int(input())
    if n == 999:
        break
    s += n
print(f'a soma é = {s}') # python 3.6 ou superior
print('a soma é = {}'.format(s)) # python 3
print('a soma é = %d' %(s)) # python 2



nome = 'Pedro'
salario = 999.8
print(f'o salario do {nome:-^20} é = {salario:.1f}')
print('o salario do {} é = {}'.format(nome,salario))
print('o salario do %s é = %.2f'%(nome,salario))



#Desafio 66

nro = soma = con = 0
while True:
    nro = int(input())
    if nro == 999:
        break
    con +=1
    soma += nro
print(f'vc digitou {con} numeros dando a soma de {soma}')


#

nro = 0
while True:
    nro = int(input())
    if nro < 0:
        break
    for x in range(11):
        print(f'{nro} X {x:2} = {nro*x}')
print('fim de jogo')


'''

#Deafio 67
from random import  randint

pc = cont = soma = verificador = 0
escolha = ''
resposta = ''
while True:
    nro = int(input('Digite um numero '))
    pc = randint(0, 9)
    soma = pc + nro
    verificador = soma % 2
    if verificador == 1:
        resposta = "IMPAR"
    else:
        resposta == 'PAR'
    escolha = input('Escolha Par ou Impar').strip().upper()[0]
    print(f'vc escolheu{nro} e o computador escolheu {pc} a soma foi de {soma} que é {resposta} ' ,end = ' ')

    if escolha == 'P' and verificador == 1 or escolha == 'I' and verificador ==0:
        print(' Vc perdeu')
        break

    print(' Vc ganhou')
print('Fim de jogo')

