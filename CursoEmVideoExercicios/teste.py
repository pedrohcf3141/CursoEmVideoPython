'''
teste teste
#1003
a = int(input())
b = int(input())
print('SOMA = {}'.format(a+b))

#1002
r = float(input())
n = 3.14159
a = n*pow(r,2)
print('A={:.4f}'.format(a))

#1004
a = int(input())
b = int(input())
print('PROD = {}'.format(a*b))

#1005
a = float(input())*3.5
b = float(input())*7.5
print('MEDIA = {:.5f}'.format((a+b)/11))

#1006
a = float(input())*2
b = float(input())*3
c = float(input())*5
print('MEDIA = {:.1f}'.format((a+b+c)/10))

#1007
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print('DIFERENCA = {}'.format((a*b)-(c*d)))

#1008
a = int(input())
b = int(input())
c = float(input())
print('NUMBER = {}'.format(a))
print('SALARY = U$ {:.2f}'.format(b*c))


#1009
a = input()
b = float(input())
c = float(input())*0.15
print('TOTAL = R$ {:.2f}'.format(b+c))

1010
a = input()
b=input()
la = a.split()
lb = b.split()
a = float(la[1])*float(la[-1])
b = float(lb[1])*float(lb[-1])
print('VALOR A PAGAR: R$ {:.2f}'.format(a+b))

1011
r = int(input())
v = (4/3)*3.14159*pow(r,3)
print('VOLUME = {:.3f}'.format(v))
'''
1012
'''
a) a área do triângulo retângulo que tem A por base e C por altura. 
b) a área do círculo de raio C. (pi = 3.14159) 
c) a área do trapézio que tem A e B por bases e C por altura. 
d) a área do quadrado que tem lado B. 
e) a área do retângulo que tem lados A e B. 

#   1012
l =input().split()
a =float(l[0])
b =float(l[1])
c =float(l[2])
pi = 3.14159

print('TRIANGULO: {:.3f}'.format((a*c)/2))
print('CIRCULO: {:.3f}'.format(pi*pow(c,2)))
print('TRAPEZIO: {:.3f}'.format(((a+b)*c)/2))
print('QUADRADO: {:.3f}'.format(pow(b,2)))
print('RETANGULO: {:.3f}'.format(a*b))
'''
#1043
a,b,c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

if a >= b + c or b >= a + c or c >= b + a:
    print("Area = {:.1f}".format(((a + b) * c) / 2))
else:
    print("Perimetro = {:.1f}".format(a + b + c))