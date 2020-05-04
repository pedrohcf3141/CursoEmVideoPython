# Desafio 093

jogador = {}
jogador['Nome'] = input("Nome: ")
partidas = int(input('Partidas: '))
gols = []
total = 0
for x in range(0,partidas):
    g = int(input(f"gol na partida {x+1} "))
    gols.append(g)
    total += g
jogador['gols'] = gols
jogador['total'] = total
linha = '=-'*30
print(linha)
for c,v in jogador.items():
    print(f'O campo {c} te o valor {v}')
print(linha)
print(f' o jogador {jogador["Nome"]} jogou {partidas} partidas')
print(linha)
for x in range(0,partidas):
    print(f' => Na partida {x+1}, fez {gols[x]} ')
print(f'foi um total de {total} gols')
print(linha)