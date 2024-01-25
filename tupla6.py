listinha = []
lista = []
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input('Digite o preço: '))
    lista.append(produto)
    listinha.append(preco)
    tuplinha = tuple(listinha)
    tupla = tuple(lista)
    add = str(input("Gostaria de adicionar mais um item [S/N]?  ")).upper()
    if add == 'N':
        break


print('*' * 10)
print("TABELA")
print('*' * 10)

for i in range(len(lista)):
    print(f"{tupla[i]} ---------- {tuplinha[i]}")