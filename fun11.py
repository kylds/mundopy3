#manual de interactive help 

def msg(info):
    print('~'* len(info))
    print(info)
    print('~'* len(info))

msg('SISTEMA DE AJUDA PyHELP')

def Pyhelp(duvida):
    print('Acessando o manual da(o) {}'.format(duvida))
    help(duvida)
    print(help)

duvida = str(input("função ou biblioteca python >> "))
Pyhelp(duvida)
while duvida != 'fim':
    msg('SISTEMA DE AJUDA PyHELP')
    duvida = str(input("função ou biblioteca python >> "))
    Pyhelp(duvida)
    if duvida.upper() == 'fIM':
        msg('ATÉ LOGO!')
        break 
        

