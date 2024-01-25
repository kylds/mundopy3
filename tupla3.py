import random 
#números aleatórios 
from random import randint
# da pra add elementos numa tupla com uma lista 

#tupla = ()
#lista = []


# for i in range(5):
   # num = int(input("Digite os números: "))
    #lista = list(tupla) #list vai transformar a tupla em uma lista
    #lista.append(num)
    #tupla = tuple(lista) # tuple vai fazer o contrário de list

tupla = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f"Números: {tupla}")
print(f"Menor valor: {min(tupla)}")
print(f"Maior valor: {max(tupla)}")