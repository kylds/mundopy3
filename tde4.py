def menu(num):
    novo_n = str(num)
    if novo_n.isalpha():
        print('Erro! digite novamente')
    else:
        print('Opção: {}'.format(novo_n))
        return novo_n

def cadastro(lista):
    c = 0 
    for item in lista:
        c +=1 
        print(f'{c} - {item}')
    return lista 


def pessoas(lista1):
    for nome in range(len(lista1)):
        if nome %2 ==0:
            print(f'\n{lista1[nome]} --- ',end = '')
        else:
            print(f'{lista1[nome]}', end = ' ')