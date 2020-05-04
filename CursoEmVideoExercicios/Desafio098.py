def contador(inicio,fim,passo):
    from time import sleep
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('+='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio}',end=' ')
            sleep(0.5)
            inicio += passo
    elif inicio > fim:
        while inicio >= fim:
            print(f'{inicio}', end=' ')
            sleep(0.5)
            inicio -= passo
    print('FIM')
    print('=-' * 30)


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora sua vez personalize a sua contagem')
i = int(input('Inicío: '))
f = int(input('Fim: '))
c = int(input(('Contador: ')))
contador(i, f, c)

#Solução Guanabara, ele importou fora da def
from time import sleep
def contador2(inicio,fim,passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= -1
    print('+='*30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        while inicio <= fim:
            print(f'{inicio}',end=' ',flush=False)
            sleep(0.5)
            inicio += passo
    elif inicio > fim:
        while inicio >= fim:
            print(f'{inicio}', end=' ',flush=False)
            sleep(0.5)
            inicio -= passo
    print('FIM')
    print('=-' * 30)


contador2(1, 10, 1)
contador2(10, 0, 2)
print('Agora sua vez personalize a sua contagem')
i = int(input('Inicío: '))
f = int(input('Fim: '))
c = int(input(('Contador: ')))
contador2(i, f, c)

