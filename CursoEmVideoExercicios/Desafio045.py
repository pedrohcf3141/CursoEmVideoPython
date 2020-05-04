# Desafio 45

from time import sleep
from random import randint

def espera():
    sleep(0.5)

def linha():
    print('-='*35)

computador = randint(1,3)
dicionario = {1:'PEDRA',2:'PAPEL',3:'TESOURA'}


linha()
print('''
Suas opções
[1] PEDRA
[2] PAPEL
[3] TESOURA 
''')
linha()
pessoa = int(input('SUA JOGADA'))
print('JO')
espera()
print('KEN')
espera()
print('PO')
linha()
if computador < pessoa or computador == 3 and pessoa ==1:
    print("Pessoa ganhou")
    linha()
elif computador > pessoa or pessoa == 3 and computador ==1:
    print('Computador ganhou')
else:
    print('Empatou')

print('Pessoa escolheu {} e computador escolheu {}'.format(dicionario[pessoa],dicionario[computador]))



