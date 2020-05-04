#Desafio 80
lista = []
for cont in range(0,5):
    nro = int(input('Digite um valor: '))
    if cont == 0 or nro > max(lista):
        lista.insert(len(lista),nro)
        print('Adicionado no final da lista')
    else:
        for i in range(len(lista)):
            if nro <= lista[i]:
               lista.insert(i,nro)
               print(f'Adicionado na posição {i}')
               break

print('=-'*30)
print(f'Os valores digitados foram {lista}')


