#Desafio 89

#lista[[nome,[nota1,nota2,media]]]
lista = []
aluno = []
notas = []
while True:
    aluno.append(input("Nome: "))
    notas.append(float(input("Nota 1: ")))
    notas.append(float(input("Nota 2: ")))
    notas.append(round((notas[0] +   notas[1])/2,1))  # média
    aluno.append(notas[:])
    lista.append(aluno[:])
    notas.clear()
    aluno.clear()
    resposta = input("Deseja continuar? [S/N]")
    if  resposta in "Nn":
        break
print(30*"=-")
print(f'{"NO":<4} {"NOME":<10} {"MÉDIA":>8}')
for nro,elemento in enumerate(lista):
    print(f"{nro:<4} {elemento[0]:<10}   {elemento[1][2]:>10}")
while True:
        num = int(input("Mostrar a nota de qual Aluno? (999 para parar)"))
        if num == 999:
            break
        elif num >= len(lista):
            print("Valor invalido, digite outro ou 999 para parar")
        else:
            print(f"Notas de {lista[num][0]} foram {lista[num][1][0]} e {lista[num][1][1]}")
print("finalizado")