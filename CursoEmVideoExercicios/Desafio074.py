# Desafio 74

import random

tupla = (random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100),random.randint(0,100))
tuplaArrumada = sorted(tupla)
print(f"os valores selecionados são = {tupla[0]} {tupla[1]} {tupla[2]} {tupla[3]} {tupla[4]} ")
print(f"O maior valor é {tuplaArrumada[-1]} ")
print(f"O menor valor é {tuplaArrumada[0]}")
# solução do Guanabara para o maior e o menor
print(f"O maior usando o max é {max(tupla)}")
print(f"O menor usando min é {min(tupla)}")

