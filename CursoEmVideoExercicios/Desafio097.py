def texto(txt):
    tamanho = len(txt) + 4
    print('~'*tamanho)
    print(f'  {txt}')
    print('~' * tamanho)


texto('Pedro')
texto('Ola Mundo')
texto('oi')