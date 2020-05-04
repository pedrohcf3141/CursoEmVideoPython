# Desafio 37


nro = int(input('numero '))
print()
escolha = int(input('1 para binario, 2 para octal e 3 para hexadecimal'))
lista = []
conversor = 10
hexa = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}


if escolha == 1:
    conversor = 2
elif escolha == 2:
    conversor = 8
elif escolha == 3:
    conversor = 16

while nro > 0:
    x = nro % conversor
    if x in hexa:
        x = hexa[x]
    lista.append(x)
    nro = nro // conversor




nro = int(input('numero '))
escolha = int(input(''' 
1 para binario 
2 para octal 
3 para hexadecimal'''))

if escolha == 1:
    print(str(bin(nro)[2:]))
elif escolha == 2:
    print(str(oct(nro)[2:]))
elif escolha == 3:
    print(str(hex(nro)[2:]))
else:
    print('opção invalida')








lista = lista[::-1]
nro = str(lista).replace(",", "").replace('[', '').replace(']', '').replace(' ', '').replace("'","")
print(nro)

