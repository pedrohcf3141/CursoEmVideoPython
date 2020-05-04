def area(a,b):
    area = a*b
    print(f'A área  de um terreno {a:.2f} x {b:.2f} é de {area}m2')

print('Controle de terrenos')
print('-'*30)
l = float(input('LARGURA (m): '))
c = float(input('CONMPRIMENTO (m): '))
area(l,c)
