# Ajuda Interativa
print(input.__doc__)

help(input)

def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM')

contador(2, 10, 2)
help(contador)

# Parametros Opcionais

def soma(a=0, b=0, c=0):
    """
    -> soma 3 numeros
    :param a: primeiro numero, parametro opcional
    :param b: segundo numero, parametro opcional
    :param c: terceiro numero, parametro opcional
    :return: sem retorno
    """
    print(f'{a+b+c}')

soma(1, 2, 3)
soma(1,2)
soma(1)
soma()

help(soma)

def imprime(txt = ''):
    """
    Imprime texto na tela formatado com uma linha em cima e outra embaixo do tamanho do texto
    :param txt: texto,parametro opcional
    :return: sem retorno
    """
    print('~' * len(txt))
    print(txt)
    print('~' * len(txt))

imprime('Pedro')

imprime()

imprime('OI')

help(imprime)

# Escopo de Variaveis
    #n Variavel Global
    #x Variavel Local
def teste():
    global p
    p = 100
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')
    print(f'Na função teste p vale {p}')

    #Programa Principal
n = 2
x = 4
p = 10

teste()

print(f'No progama principal n vale {n}')
print(f'No progama principal x vale {x}')
print(f'No progama principal p vale {p}')

def mult (a=1,b=1, c=1):
    m = a * b * c
    return m


print(mult(2,2))


# parte pratica

print()
def fat(nro =1):
    f = 1
    for c in range(nro, 0, -1):
        f *= c
    return f
print(fat(5))