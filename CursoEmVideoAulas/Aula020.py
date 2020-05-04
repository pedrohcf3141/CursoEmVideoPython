def titulo(texto):
    print('-'*30)
    print(texto)
    print('-' * 30)


titulo('    CURSO EM VIDEO    ')
titulo(texto = '    CURSO EM VIDEO    ')


def contador(* num):
    print(len(num))
    print(num)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos] *= 2
        pos +=1


valores = [7,2,5,0,4]

print(valores)
dobra(valores)
print(valores)


def soma(* val):
    soma = 0
    for nro in  val:
        soma += nro
    print(soma)

soma(2,4,5)
soma(1, 2)
soma(7)
soma()
