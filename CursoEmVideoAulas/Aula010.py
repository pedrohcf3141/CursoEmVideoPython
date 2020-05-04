#Condições if e else


ano = int(input('Ano do carro '))

if ano <= 3 :
    print('Carro novo')
else:
    print('Carro velho')
print('fim')

print('carro novo' if ano <=3 else 'carro velho')
print('fim')
