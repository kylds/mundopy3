lista = []
maior = 0 
menor = 0
for i in range(5):
    num = int(input("Digite um número: "))
    lista.append(num)
    maior = max(lista)
    menor = min(lista)
    #if i == 0:
      #  maior == menor == lista[i]
    #else:
     #   if lista[i] > maior:
      #      maior = lista[i]
       # if lista[i] < menor:
        #    menor = lista[i]

#for c, v in enumerate (lista):
    #if v == maior:
        #print(f'posição {i}', end = '')
#print(f"Maior número: {maior}, posição na lista: ", end = '')
#print(f"Menor número: {menor}, posição na lista: ", end = '')
# for c, v in enumarate (lista):
# if v == menor:
# print(f'posição: {i}', end = '')

print(f"Números digitados: {lista}")
print(f"Maior número: {maior}, posição na lista: {lista.index(maior)}")
print(f"Menor número: {menor}, posição na lista: {lista.index(menor)}")