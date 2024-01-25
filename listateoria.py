lanche = ('suco','leite','refri')
# tuplas são imutaveis então se quiser mudar os elementos 
# é preciso utilizar uma lista 
lanche = ['suco', 'leite','pudim']
#para add elementos na lista:
lanche.append('cookie')
#para adicionar o elemento em uma posição especifíca:
lanche.insert(0,'cachorro-quente')
# para eliminar o elemento em uma posição específica:
# depois que ele remoe ele reajusta os indices 
# para apagar algo utiliza-se o pop()
lanche.pop(3)
del lanche[3] 
lanche.remove('pizza')
# para declarar uma lista com uma variável:
valores = list(range(4,11))
valores = ['8,2,5,4,9,,3,0']
# organizar os valores da lista:
valores.sort()
# organizar na ordem inversa:
valores.sort(reverse = True)
# saber o tamanho da lista:
len(valores)
# encontrar a posição de um elemento:
lanche.index('9')
# uma funçã que verifica a sequência (lista,tupla,string)
# e ao mesmo tempo acompanha o índice durane a iteração:
lista = ['maçã', 'banana', 'laranja', 'morango']
for indice, fruta in enumerate(lista):
    print(f"O índice {indice} corresponde a {fruta}")
# [:] - fatiamento completo dos dados

#uma lista com vários elementos, ou seja listas compostas 
# tira print dessa forma:
pessoas = [['pedro',25], ['maria', 19], ['joão', 32]]
print(pessoas[0][0]) # vai tirar print do indice zero e o que está no zero
for p in pessoas:
    print(f'{p[0]} tem {p[1]} de idade') 
pessoas.clear() # apagar os dados 
