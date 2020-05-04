# Desafio 55


maior = 0
menor = 0
for x in range(1, 6):
    peso = float(input('peso da pessoa {} '. format(x)))
    if x ==1:
        maior = peso
        menor = peso

    if peso >= maior:
        maior = peso

    elif peso <= menor:
        menor = peso
print('MAIOR {} \nMENOR {}'.format(maior, menor))


