lista = []
#REVER!

for i in range(5):
    num = int(input('Digite os números: '))
    lista.append(num)
    if num[i + 1] > num[i]:
        num[i],num[i + 1] = num[i + 1], num[i]

print(f"Lista: {lista}")

    

#bubble sort - organiza a lista em ordem crescente 
# para por em ordem decrescente é só fazer o contrário
for c in range(len(lista)):
    for j in range(0,len(lista)-c-1):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]