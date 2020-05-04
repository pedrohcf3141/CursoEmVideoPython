lista = list()
pessoa = dict()

while True:
    pessoa['nome'] = input('Nome: ')
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').upper()[0]
        if pessoa['sexo'] in 'FM':
            break
        print('erro digite apenas M ou F ')
        print()
    pessoa['idade'] = int(input('Idade: '))
    lista.append(pessoa.copy())


    while True:
        resposta = input('Deseja continuar: [S/N]').upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Respostas apenas S ou N')
    if resposta in 'Nn':
            break
cont = len(lista)
soma = 0

for x in lista:
    soma += x['idade']
media = soma/cont
print(f'A) Ao todo foram cadastrados {cont} pessoas')
print(f'B) A medias das idade foi {media:5.2f} anos')
print(f'C) As mulheres casdastadas foram',end=' ')
for x in lista:
    if x['sexo'] in 'Ff':
        print(f'{x["nome"]}',end=' ')
print()
print(f'D) Lista das pessoas acima da média')
for x in lista:
    if x['idade'] >= media:
        print('          ')
        for k,v in x.items():
            print(f'{k} = {v}',end=" ")
        print()
print('<<<ENCERRADO>>>')