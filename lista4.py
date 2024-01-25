lista = []

while True:
    num = int(input("Digite os números: "))
    add = str(input("Quer continuar [S/N]: ")).upper()
    if add == 'N':
        break
    else:
        lista.append(num)

if 5 in lista:
    print("O número 5 está na lista")
else:
    print("O número 5 não está na lista")

for i in range(len(lista)):
    for c in range(0,len(lista)-i-1):
        if lista[c] > lista[c+1]:
            lista[c+1], lista[c] = lista[c], lista[c+1] 

print(f"Lista: {lista}")
print(f"Quantidade de números digitados: {len(lista)}")
