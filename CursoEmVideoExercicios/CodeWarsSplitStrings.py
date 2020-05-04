def solution(s):
    if len(s)%2 != 0:
       s +="_"
    cont = 0
    lista = []
    while cont < len(s):
        lista.append(s[cont]+s[cont+1])
        cont += 2

    return lista

print(f" {solution('abc')} \n {solution('abcdef')}")

#Solução Melhor
def solution(s):
# não coloca o !=
    if len(s)%2:
       s +="_"
    cont = 0
    lista = []
    for i in range(0,len(s),2):
        lista.append(s[i:i+2])

    return lista

print(f" {solution('abc')} \n {solution('abcdef')}")
