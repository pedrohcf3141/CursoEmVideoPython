#Desafio 31

km = float(input('km da viagem '))
if km <= 200:
    print('o valor da viagem será de R$ {:.2f}'.format(km * 0.5))
else:
    print('o valor da viagem será de R$ {:.2f}'.format(km * 0.45))



