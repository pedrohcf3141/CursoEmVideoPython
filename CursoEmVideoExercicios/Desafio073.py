#Desafio 73

lista = ('Flamengo','Santos','Palmeiras','Corinthians','São Paulo','Internacional','Bahia','Atlético-MG','Athletico-PR','Botafogo','Grêmio','Ceará','Fortaleza','Goiás','Vasco','Cruzeiro','Fluminense','CSA','Chapecoense','Avaí')
linha = "-*"*50
print(f"Lista do Campeonato {lista}")
print(linha)
print(f"Os 5 primeiros são{lista[:5]}")
print(linha)
print(f"Os 4 ultimos são{lista[-4:]}")
print(linha)
print(f"Os times em ordem alfabética são{sorted(lista)}")
print(linha)
print(f"O Chapecoense está na {lista.index( 'Chapecoense')+1} posição")
print(linha)

