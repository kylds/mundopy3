#mega sena
from random import randint 
from time import sleep 
print("*" * 10)
print("Mega sena")
print("*" * 10)
lista = []
jogo = int(input("Quantos jogos? "))

for i in range(jogo):
    for aleatorio in range(6):
        numeros = randint(1,60) 
        lista.append(numeros)
        sleep(1)
    print(f"Jogo {i+1} --------- {lista}")
    lista = list()    




