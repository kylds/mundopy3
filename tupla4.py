tupla = ()
lista = []
cont = 0
pares = []



for i in range(4):
    num = int(input("Digite os números: "))
    lista = list(tupla)
    lista.append(num)
    tupla = tuple(lista)
    if num == 9:
        cont +=1 
    elif num == 3:
        n = tupla.index(3)
    elif num % 2 == 0:
        pares.append(num)

print(f"Quantidade de números de 9: {cont}")
print(f"O número três aparece na posição {n}")
print(f"Pares: {pares}")
