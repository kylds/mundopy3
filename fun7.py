#fatorial
from math import factorial 
from time import sleep 
def fatorial(numero,show):
    """
    ---> Calcular o fatorial de um número:
    ;numero: o valor que tera o fatorial resolvido
    ;show: observar por completo o processo fatorial

    """
    num = factorial(numero)
    for fat in range(numero,0,-1): 
        if show == True:
            sleep(0.5)
            print('{}'.format(fat), end = '', flush = True)
            if fat > 1:
                print('x', end = '', flush = True)
            else:
                print(' = {}'.format(num), end = '', flush = True)
        else:
            print(num) 
fatorial(4,show=True)
