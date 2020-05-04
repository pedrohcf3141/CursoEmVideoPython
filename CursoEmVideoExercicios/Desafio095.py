jogador = {}
time = []
while True:
    jogador.clear()
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
    time.append(jogador.copy())

    while True:
        resposta = input('Deseja continuar? [S/N]').upper()[0]
        if resposta in'SN':
            break
        print('Resposta Invalida, responda S ou N')
    if resposta == 'N':
        break
print('=-'*40)
print('cod',end=' ')
for i in jogador.keys():
    print(f'{i:<15}',end='')
print()
for chave,valor in enumerate(time):
    print(f'{chave:>3} ',end='')
    for dado in valor.values():
        print(f'{str(dado):<15}',end='')
    print()
print('=-'*40)
while True:
    while True:
        jog = int(input('Mostrar dados de qual jogador? (999 para parar)'))
        if jog in range(0,len(time)) or jog == 999:
            break
        print(f'Erro o jogador com código {jog} não esta na lista')
    if jog == 999:
        print('<<<VOLTE SEMPRE>>>')
        break
    print(f'Analize do jogador {time[jog]["Nome"]}')
    print(f' o jogador {time[jog]["Nome"]} jogou {len(time[jog]["gols"])} partidas')
    print(linha)
    for x in range(0,len(time[jog]["gols"])):
        print(f' => Na partida {x+1}, fez {time[jog]["gols"][x]} gols')
    print(linha)
