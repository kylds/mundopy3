lista = []
cont = 0
pesadas = []
menos_pesadas = mais_pesada = 0 
menos = []
while True:
    nome = str(input("Digite o nome: "))
    peso = float(input("Digite o peso: "))
    lista.append([nome,peso])
    add = str(input("Gostaria de adicionar mais alguma pessoas? [S/N]: ")).upper()
    if add == 'N':
        break 

for nome in lista:
    cont += 1  

for peso in lista:
    if peso > pesadas:
        mais_pesada = peso 
        pesadas.append(mais_pesada)
    else:
        menos_pesadas = peso
        menos.append(menos_pesadas)

print(f"Quantidade de pessoas: {cont}")
print(f"Pessoas mais pesadas: {pesadas}")
print(f"Pessoas menos pesadas: {menos}")
