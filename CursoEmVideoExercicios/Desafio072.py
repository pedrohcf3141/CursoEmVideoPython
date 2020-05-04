# Desafio 72

num = ("um","dois","tres","quatro","cinco",
       "seis", "sete","oito","nove","dez",
       "onze","doze","treze","catorze","quinze",
       "dezesseis","dezessete","dezoito","dezenove","vinte",
       "zero")
nro = int(input("Digite um numero "))
while nro not in range(len(num)):
    print(f"{nro} não conta na lista digite novamente",end=" ")
    nro = int(input())
if nro in range(len(num)):
    print(num[nro-1])

#72 oficial

num = ("zero","um","dois","tres","quatro","cinco",
       "seis", "sete","oito","nove","dez",
       "onze","doze","treze","catorze","quinze",
       "dezesseis","dezessete","dezoito","dezenove","vinte")
while True:
    nro = int(input("Digite um numero entre 0 e 20 "))
    if 0<= nro <=20:
        print(f"voce digitou {num[nro]}")
        resp = input("quer continuar? S para Sim e N para Não ")
        if resp =="N":
            break
    print("Tente novamente.", end=" ")


