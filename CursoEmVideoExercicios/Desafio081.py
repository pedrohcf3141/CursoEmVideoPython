#Desafio 81

lista = list()
while True:
    lista.append(int(input('Digite um valor ')))
    resposta = str(input('Deseja continuuar [S/N]'))
    if resposta in 'Nn':
        break

print('=-'*30)
print(f'Você digitou {len(lista)} valores')
if 5 in lista:
    lista.sort()
    print(f'Os valores em ordem crescente são {lista}')
    print('O valor 5 esta na lista')
else:
    lista.sort(reverse=True)
    print(f'Os valores em ordem decrescente são {lista}')
    print('O valor 5 não esta na lista')

