#Desafio 83
expressao =input("Digite a Expressão: ")
abre = []
fecha = []
resposta =''
for x in expressao:
    if x == "(":
        abre.append(x)
    if x == ")":
        fecha.append(x)
    if len(fecha) > len(abre):
        resposta = "Expressão Inválida"
        break
if len(fecha) == len(abre):
    resposta = "Expressão Válida"
else:
    resposta = "Expressão Inválida"
print(resposta)

# Solução Guanabara
expr = str(input("Digite sua expressão: "))
pilha = []
for simb in expr:
    if simb == "(":
        pilha.append('(')
    elif simb == ")":
        if len(pilha)>0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Válida')
else:
    print('Expressão Inválida')

