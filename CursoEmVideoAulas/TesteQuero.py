#print('Hello, World!')

#print('Hello, World!')

''''#1
lista=[]
while True:
    try:
        n = int(input())
        if n>0:
            lista.append(n)
    except:
        break
t = 1
while True:
    if t in lista:
        t += 1
    else:
        break

print(t)

lista=[]
while True:
    try:
        n = input()
        lista.append(n)
    except:
        break
if len(lista[0]) != len(lista[1]):
    print('false')

else:
    for l in lista[1]:
        if l not in lista[0]:
            r = 'false'
            break
        else:
            r = 'true'
    print(r)



#4
lista=[]
while True:
    try:
        x = int(input())
        lista.append(x)
    except:
        break
soma = lista[0]
l = lista[1]
c = 0
cont =0
del lista[0:1]

while cont <= soma:
    for x in lista:
        if soma % x ==0:
            c +=1
'''

lista=[]
lista2 =[]
lista3 =[]
while True:
    try:
        x = int(input())
        lista.append(x)
    except:
        break

n = len(lista)
s = [0]*(n+1)
k = 0
while True:
        if s[k] < n:
            s[k+1] = s[k] + 1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            for j in range(1, k+1):
                lista2.append([lista[s[j]-1]])
for i in range(len(lista2)):
        for c in lista2[:i]+lista2[i+1:]:
            lista.append([lista2[i]]+c)
menor = 0
s =0
for elemento in lista:
    for e in elemento:
        s +=int(e)
        if menor > int(s):
            lista3 =[]
            menor = s
            lista3.append(elemento)


print(lista3)


'''
3 - [SO] Subarray contíguo de menor soma
Dado um inteiro N, e um array de números inteiros, escreva um código que procura e imprime o subarray contíguo (isto é, um subconjunto de elementos adjacentes) de menor soma, contido no array original. Se a menor soma possível for não negativa, o seu código deve imprimir 0. Se existirem dois ou mais subarrays contíguos cuja soma é a menor possível, o que ocorrer primeiro deve ser impresso.

 

Entrada
 
A entrada contém um caso de teste. A primeira linha da entrada contém um número inteiro N, indicando o tamanho do Array. Seguem-se N linhas, cada uma contendo um valor do array.
 
Saída
 
A saída deve conter o subarray contíguo de menor soma. Imprima um valor do subarray por linha.

entrada
7
-2
1
-1
4
-4
3
-5
saida
-4
3
-5
entrada
4
3
2
1
0
saida
0
entrada
5
-10
10
-5
-5
20
saida
-10

4 - [SO] Combinação de moedas
Dado um valor de N centavos e um array com M valores diferentes de moedas (também em centavos), escreva um código que calcula e imprime de quantas maneiras distintas as moedas podem ser combinadas para se gerar um troco com valor N. Considere que você tem à disposição um número infinito de cada tipo de moeda, e que a ordem das moedas não interessa.

 

Entrada
 
A entrada contém um caso de teste. A primeira linha da entrada contém um número inteiro N, indicando os centavos. A segunda linha da entrada contém um inteiro M, indicando o tamanho do array de moedas, seguido de M linhas, cada uma contendo um valor diferente de moeda.
 
Saída
 
A saída deve conter apenas um número inteiro, que representa a quantidade de combinações diferentes possíveis para gerar o troco com valor N, seguido de um caractere de final de linha ("\n").
 
 
Explicação do primeiro caso do exemplo: há 4 soluções possíveis: [1, 1, 1, 1,], [1, 1, 2], [2, 2] e [1, 3]

Explicação do segundo caso do exemplo: há 5 soluções possíveis: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 2, 6], [2, 3, 5], [5, 5]   

entrada
4
3
1
2
3
saida
4

entrada
10
4
2
5
3
6
saida
5



'''