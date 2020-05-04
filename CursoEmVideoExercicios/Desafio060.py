# Desafio 60

fat = int(input())
cont = fat
m = 1

while cont > 0:
    print(' {} '.format(cont),end="")
    print("x" if cont > 1 else "=", end="")
    m *= cont
    cont -= 1


print(m)


