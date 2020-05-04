n = 1
par = impar = 0
while n != 0:
        if n != 0:
            n = int(input("Digite um numero e 0 para sair "))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Pares {} \nImpares {}".format(par,impar))
