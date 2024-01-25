#aprimorando o dic4 
#jogador de futebol 


jogadores = []

while True:
    lista_gols = [] #tem quer ser dentro para que cada jogador tenha uma lista própria de gols, se for fora fica uma variável global
    jogador = str(input("Digite o nome do jogador: "))
    partidas = int(input("Digite a quantidade de partidas jogadas pelo jogador: "))
    for partida in range(partidas):
        gols = int(input(f"Digite a quantidade de gols feitos na {partida+1} partida: "))
        lista_gols.append(gols)
    jogadores.append({f'Nome': jogador, 'Quantidade de gols por partida': lista_gols})
    add = str(input("Deseja adicionar mais algum jogador? [S/N]: ")).upper()
    if add != 'S' and add != 'N':
        print("ERRO! Digite novamente")
        add = str(input("Deseja adicionar mais algum jogador? [S/N]: ")).upper()
    if add == 'N':
        break 


for jogador in range(len(jogadores)):
    soma = 0 #para cada somatorio tem que ter um dele, mesmo coisa da lista_gols 
    print("Informações gerais do jogador:")
    print(jogadores[jogador])
    print()
    print('-'* 10)
    gols_do_jogador = jogadores[jogador]['Quantidade de gols por partida'] #lista de jogadores - n é um int ou uma string é um dic, ent acessa a key do dic que corresponde a lista de gols feita por partida
    for gols in range(len(gols_do_jogador)):
        soma += gols_do_jogador[gols]
        print('=> Na {} partida, fez {} gols'.format(gols+1,jogadores[jogador]['Quantidade de gols por partida'][gols]))
    print("Quantidade total de gols: {}".format(soma))

