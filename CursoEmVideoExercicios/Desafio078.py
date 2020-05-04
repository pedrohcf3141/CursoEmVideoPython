# Desafio 78

lista = []
x = 0
while x < 5:
    lista.append(int(input(f'Insira um valor na posição {x}: ')))
    x += 1
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi{max(lista)} nas posições',end=' ')
x = 0
for c in lista:
    if c == max(lista):
        print(f'{x}',end='... ')
    x+=1
print()
print(f'O menor valor digitado foi{min(lista)} nas posições',end=' ')
x=0
for c in lista:
    if c == min(lista):
        print(f'{x}',end='... ')
    x+=1

# Desafio 78 solução Guanabara
lista =[]
menor = 0
maior = 0
for c in range(0,5):
    lista.append(int(input(f'Insira um valor na posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print(f'O maior valor digitado foi{maior} nas posições',end=' ')
for i,v in enumerate(lista):
    if v == maior:
        print(f'{i}... ',end='')

print(f'\nO menor valor digitado foi{menor} nas posições',end=' ')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}... ',end='')

