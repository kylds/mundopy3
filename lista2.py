print('-' * 10)
print("CADASTRO")
print('-' * 10)

lista = []
while True:
    num = int(input("Digite os números: "))
    if num not in lista:
        lista.append(num)
    else:
        print("Valor duplicado! valor não adicionado")
    add = str(input("Quer adicionar mais números? [S/N]: ")).upper()
    if add == 'N':
        break 
          
lista.sort()
print(f"Números digitados: {lista}")

# if num not in lista - se não estiver dentro da lista adiciona 
# agr se já estiver ai ele não vai adicionar por isso o else 