#Desafio 79
lista = []
resposta =''
lista.append(int(input('Digite um Valor')))
while True:
    resposta = input('Quer Continuar [S/N]').upper()
    if resposta == 'N':
        break
    if resposta == 'S':
        resposta = int(input('Digite Outro valor: '))
        if resposta in lista:
            print(f'O valor {resposta} ja consta na lista e não foi adicionado')
        else:
            lista.append(resposta)
    else:
        print(('essa reposta não é valida'))
lista.sort()
print(f'o valores digitados foram {lista}')


