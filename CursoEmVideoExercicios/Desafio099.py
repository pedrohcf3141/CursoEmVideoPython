def maior(* nro):
    from time import sleep
    maior = contador = 0
    print('=-' * 40)
    print('Analizando os valores passados')
    if len(nro) == 0:
        mai = 0
    else:
        mai = max(nro)
    for item in nro:
        print(item, end=' ')
        sleep(0.5)
        if item > maior:
            maior = item
        contador += 1
    print(f'Foram informados {len(nro)} valores ao todo.(len)')
    print(f'O maior valor informado é o {mai} (função max)')
    print('=-'*30)
    print(f'Foram informados {contador} valores ao todo.(contador)')
    print(f'O maior valor informado é o {maior} (maior)')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
