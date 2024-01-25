lista = []
while True:
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    add = str(input("Deseja digitar mais algum aluno? [S/N]: ")).upper()
    lista.append([nome,nota])
    if add == 'N':
        break 
    else:
        aluno = str(input("Deseja buscar a nota de algum aluno? [S/N]: ")).upper()
        digite = str(input("Digite o nome do aluno: "))
        if digite in [nome for aluno in lista]: 
            print(f"Aluno: {nome} ------- nota: {nota}")
        else:
            print("Aluno não encontrado")
        
        
print('=' * 15)
print("BOLETIM")
print('=' * 15)
for i in range(len(lista)):
    print(f"{nome} --------- {nota}")
    
   



nome = []
peso = []
mais_pesadas = []
menos_pesadas = []


while True:
    n = input("Digite o nome: ")
    p = float(input("Digite o peso: "))
    nome.append(n)
    peso.append(p)
    add = str(input("Deseja adicionar mais pessoas? [S/N]: ")).upper()
    if add == 'N':
        break 
    maior_peso = max(peso)
    menor_peso = min(peso)
for i in range(len(peso)):
      if peso[i] == maior_peso:
          mais_pesadas.append(nome[i])
      else:
           menos_pesadas.append(nome[i])


print(f"Quantidade de pessoas: {len(nome)}")
print(f"Pessoas mais pesadas: {mais_pesadas}")
print(f"Pessoas menos pesadas: {menos_pesadas}")




 

 #matriz 3x3
#REFAZER! 
#matriz é uma lista dentro de outra lista 

lista = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
soma_t = 0
for j in range(3): #tem que fazer separado como se fosse linha e coluna
    for i in range(3):
        num = int(input("Digite um valor para {j} e outro para {i}: "))
        lista[j][i] = num 

for linha in lista:
    for elemento in linha:
        if elemento % 2 == 0:
            soma += elemento 

for l in range(0,3):
    for c in range(0,3):
        print(f"{lista[l][c]}")
print(f"Soma dos valores pares: {soma}")



#[0,0] [0,1], [0,2]
#[1,0], [1,1], [1,2]
#[2,0], [2,1], [2,2]



lista = []
while True:
    nome = str(input("Digite o nome: "))
    nota = float(input("Digite a nota do aluno: "))
    add = str(input("Deseja adicionar mais algum aluno? [S/N]: ")).upper()
    lista.append([nome,nota]) #criar uma lista composta 
    if add == 'N':
        aluno = str(input("Deseja observar a nota de algum aluno específico? [S/N]: ")).upper()
        if aluno == 'S':
            nome_aluno = str(input("Digite o nome do aluno: "))
            encontrado = False
            for nome_aluno in [nome for aluno in lista]:
                    print(f"{nome[0]} ---------- {nota}")
                    encontrado = True 
                    break
            if nome_aluno not in lista:
                 print("Aluno não encontrado")
            break 
        


print("-=" * 15)
print("BOLETIM")
print("-=" * 15)

for nome in lista:
    for nota in lista:
        print(f"{nome} ---------- {nota}")

