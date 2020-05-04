
# Desafio 17
from math import sqrt,hypot
co = float(input('cateto oposto '))
ca = float(input('cateto adjacente '))
hip = sqrt((pow(co,2)+pow(ca,2)))
print('o valor da hip é {:.2f}'.format(hip))
print('o valor da hip é {:.2f}'.format(hypot(co,ca)))
