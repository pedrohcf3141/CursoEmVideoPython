#Desafio 11

largura = int(input('largura = '))
altura = int(input('altura = '))
area = altura * largura
if area // 2 == 0:
    latas = area / 2
else:
    latas = int(area / 2 + 1)
print('a parede tem {}  metros quadrados e presisa de {} latas de tinta'.format(area,latas))
