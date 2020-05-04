# Desafio 26

frase = input('Digite uma frase ').strip().lower()
print('A aparece {} vezes'.format(frase.count('a')))
print('A aparece na {} casa da primeira vez'.format(frase.find('a')+1))
print ('A aparece na {} casa da ultima vez'.format(frase.rfind('a')+1))
