# Desafio 75

# minha solução
n1 = int(input("Digite um valor "))
n2 = int(input("Digite outro valor "))
n3 = int(input("Digite mais um valor "))
n4 = int(input("Digite o ultimo valor "))
tupla =(n1,n2,n3,n4)
nove = 0
for n in tupla:
    if  n == 9:
        nove+=1

print(f"Voce digitou os valores {tupla}")
print(f"Voce digitou o 9 {nove} vezes")
if 3 in tupla:
    print(f"O Valor 3 aparece na {tupla.index(3)+1} a posição ")
else:
    print("O valor 3 não foi digitado")
print("Os valores pares digitados são: ",end=" ")
for x in tupla:
    if x % 2 == 0:
        print(x,end=" ")


# solução Guanabara
tuplaG = (int(input("Digite um valor ")),int(input("Digite outro valor ")),int(input("Digite mais um valor "))
          ,int(input("Digite o ultimo valor ")))

print(f"Voce digitou os valores {tuplaG}")
print(f"Voce digitou o 9 {tuplaG.count(9)} vezes")
if 3 in tuplaG:
    print(f"O Valor 3 aparece na {tupla.index(3)+1} a posição ")
else:
    print(" O valor 3 nao foi digitado")
print("Os valores pares digitados são: ",end=" ")
for x in tupla:
    if x % 2 == 0:
        print(x,end=" ")

