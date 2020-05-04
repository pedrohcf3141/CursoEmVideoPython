#Desafio 52

nro = int(input('numero '))


for x in range(2, nro // 2):
    if nro % x == 0:
        resposta = 'NÃO É PRIMO'
        break
    else:
        resposta = 'É PRIMO'
print(resposta)


frase = input('frase ')
frase2 = frase.strip().lower().replace(' ', '')
if frase2 == frase2[::-1]:
    print('Palindromo')
else:
    print('Não é Palindromo')


from datetime import date
menor = 0
maior = 0
for x in range(1, 8):
    print('ano do nascimento da pessoa {}'. format(x), end=" ")
    ano = int(input())
    if ano <= date.today().year -21:
        maior += 1
    else:
        menor += 1
print('Temos {} MAIORES e {} MENORES'.format(maior, menor))


