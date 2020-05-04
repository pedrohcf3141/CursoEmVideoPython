# Desafio 18

from math import cos, sin, tan, radians

angulo = float(input('Digite o angulo desejado '))

print(' o seno de {} é {:.2f}'.format(angulo, sin(radians(angulo))))
print(' o coseno de {} é {:.2f} '.format(angulo, cos(radians(angulo))))
print('a tangente de {} é {:.2f}'.format(angulo, tan(radians(angulo))))

