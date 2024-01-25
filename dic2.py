from random import randint 
from time import sleep 
from operator import itemgetter
lista_dado = []
cont = 0
print('*' * 12)
print("Jogando o dado")
print('*' * 12)
for jogadores in range(4):
    valor = {f'Jogador 1': randint(0,6),
             f'Jogador 2': randint(0,6),
             f'Jogador 3': randint(0,6),
             f'Jogador 4': randint(0,6)}
sleep(0.5)
for k, v in valor.items():
    cont += 1
    sleep(0.5)
    print(f" {cont} lugar: {k} tirou {v}")

print('*' * 8)
print("Ranking dos jogadores: ") #organizar o dicionário
ranking = sorted(valor.items(), key = itemgetter(1), reverse = True)
print('*' * 8)

for i, l in enumerate(ranking):
    sleep(0.5)
    print(f'{i+1} lugar: {l[0]} com {l[1]}')

#outra maneira de organização: 
# for m in range(len(lista_dado)):
 #   for c in range(0,(len(lista_dado) - m - 1)):
#        if lista_dado[c+1] > lista_dado[c]:
 #           lista_dado[c], lista_dado[c+1] = lista_dado[c+1],lista_dado[c]
  #      numeros = {f'Jogador 1':{lista_dado[0]},
   #                'Jogador 2': {lista_dado[1]},
    #               'Jogador 3': {lista_dado[2]},
     #              'Jogador 4': {lista_dado[3]}
      #             }










