# Desafio 77


tupla = ('pedro','irene', 'python','luna','murphy','isabela','ana','atento','java','curso')
vogais = ('a','e','i','o','u')

for palavra in tupla:
    print(palavra,end=" tem as vogais: ")
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra,end=" ")
    print()
# solução ganabara

for palavra in tupla:
    print(f'\n na palavra {palavra} temos ',end="")
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')


