from random import randint 
from time import sleep 


numeros = []


def sorteia(numeros):
    for sorteio in range(5):
        sleep(0.5)
        numeros.append(randint(0,20))
    print('Os números sorteados foram {} \n E a quantidade de números foi {}'.format(numeros,sorteio+1))

print('----------------------------------')    
soma = 0
def somaPar(soma):
    for sum in range(len(numeros)):
        sleep(0.5)
        if numeros[sum] % 2 == 0:
            soma += numeros[sum]
    print('Somando os valores pares de {} temos {}'.format(numeros,soma))

sorteia(numeros)
somaPar(soma)