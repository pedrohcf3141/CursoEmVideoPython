#Desafio 92
import datetime
trabalhador = dict()
trabalhador['nome'] = str(input("Nome: "))
data = input("Ano de Nascimento(DD/MM/AAAA): ")
data1 = data.split("/")
nascimento = datetime.date(int(data1[2]),int(data1[1]),int(data1[0]))
hoje = datetime.date.today()

validadorAno = datetime.date(hoje.year,int(data1[1]),int(data1[0]))

if validadorAno <= hoje:
    idade = hoje.year - nascimento.year
else:
    idade = hoje.year - nascimento.year - 1
trabalhador['idade'] = idade
trabalhador['ctps'] = str(input('CTPS[0 caso não tenha]: '))
if  trabalhador['ctps'] != '0':
    trabalhador['salário'] = float(input('Salário: '))
    contratacao = int(input('Ano de contratação: '))
    trabalhador['aposentadoria'] = (contratacao - nascimento.year) + 35
for  k,v in trabalhador.items():
    print(f'{k} tem o valor {v}')