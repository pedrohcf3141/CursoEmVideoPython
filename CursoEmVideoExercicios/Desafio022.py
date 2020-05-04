# Desafio 22

nome = input('Digite seu nome ').strip()
#nome = 'Paulo de Souza Marques' # teste pra não ficar digitando o nome
pNome = nome.split(" ")
print('seu nome com as letras maisculas {}'.format(nome.upper()))
print('seu nome com as letras minusculas {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome)-nome.count(" ")))
print('seu primeiro nome é {} e tem {} letras'.format(pNome[0],len(pNome[0])))

