#jogador de futebol 
from time import sleep
lista_g = []
soma = 0
while True:  
    jogador = str(input("Digite o nome do jogador: "))
    partidas = int(input("Digite quantas partidas foram jogadas: "))
    for c in range(partidas):
        gols = int(input(f"Digite a quantidade gols feitos na {c+1} partida: "))
        lista_g.append(gols)
        soma += gols
    jogatina = {f"Nome do jogador": jogador,
                "Quantidade de partidas": partidas,
                "Total de gols no campeonato": soma}
    add = str(input("Deseja digitar algum jogador? [S/N]: ")).upper()
    print("-" * 10)
    for k, v in jogatina.items():
        sleep(0.5)
        print(f"{k} é {v}")
        print("-" * 10)
    print(f"O jogador {jogador} jogou {partidas} partidas")
    print("-" * 10)
    for j in range(partidas):
        sleep(0.5)
        print(f"=> Na {j+1} partida, fez {lista_g[j]} gols")
        print("-" * 10)
    if add == 'N':
        break 
    
