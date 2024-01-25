#matriz 3x3
#uma matriz é uma lista dentro de uma lista 

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma = soma_t = maior = 0
#uma matriz é dividida em linha e coluna 

for linha in range(0,3):
    for coluna in range(0,3):
        num = int(input(f"Digite um número para {linha} e outro para {coluna}: "))
        matriz[linha][coluna] = num 

for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]}]")

for p in range(0,3):
    for i in range(0,3):
        if matriz[p][i] % 2 == 0: #tem que ser desse jeito para somar totalmente certo 
            soma += matriz[p][i]
print(f"Soma dos valores pares: {soma}")
        
for linha in range(0,3): #soma dos números da terceira coluna 
    soma_t += matriz[linha][2] # o 2 é para indicar a coluna 
print(f"Soma dos valores da tecerira coluna: {soma_t}")

for coluna in range(0,3): #ver o maior elemento da segunda linha 
    if coluna == 0:
        maior = matriz[linha][coluna]
    elif matriz[linha][coluna] > maior:
        maior = matriz[linha][coluna]

print(f"Maior elemento da segunda linha: {maior}")