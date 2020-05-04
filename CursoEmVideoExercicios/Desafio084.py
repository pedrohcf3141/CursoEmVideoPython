#Desafio 84
pessoa = []
lista = []
contador = menor = maior = 0
resposta = ''
while True:
    pessoa.append(input("Nome: "))
    pessoa.append(float(input("Massa: ")))
    lista.append(pessoa[:])
    if maior<= pessoa[1]:
        maior = pessoa[1]
    if menor >= pessoa[1] or menor == 0:
        menor = pessoa[1]
    pessoa.clear()
    contador += 1
    resposta = input("Desja continuar[S/N]: ")
    if resposta.upper() == 'N':
        break
print('-='*30)
print(f'Ao todo você cadastrou {contador} pessoas')
print(f'O maior peso digitado foi {maior}. Peso de ', end='')
for pessoas in lista:
    if pessoas[1] == maior:
        print(pessoas[0], end=' ')
print()
print(f'O menor peso digitado foi {menor}. Peso de ', end='')
for pessoas in lista:
    if pessoas[1] == menor:
        print(pessoas[0], end=' ')


