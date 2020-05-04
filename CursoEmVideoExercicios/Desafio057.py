#Desafio 57

generos = ['M',"F"]
sexo = str(input("Digite seu sexo M/F: ").strip().upper())[0]
while sexo not in generos:
    print("Inserçao invalida")
    sexo = input("Digite seu sexo M/F: ").strip().upper()[0]


