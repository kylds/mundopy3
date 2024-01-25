def função(nome = 0,gols=0):
    """
    ---> Informações:
    ;nome: nome do jogador 
    ;gols: gols marcados pelo jogador

    """
    info = {'Nome': nome, 'Gols': gols}
    if nome != '' and gols != '':
        print('O jogador {} fez {} gols no campeonato'.format(nome,gols))
    elif nome == '' and gols == '':
        print('O jogador <desconhecido> fez 0 gols no campeonato')
    elif nome == '':
        print('O jogador <desconhecido> fez {} gols no campeonato'.format(gols))
    elif gols == '':
        print('O jogador {} fez 0 gols no campeonato'.format(nome))
    return info 

nome = input('Digite o nome do jogador: ')
gols = input('Digite a quantidade de gols: ')
resp = função(nome,gols)