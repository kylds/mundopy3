lista = []
tupla = ()

for i in range(5):
    num = int(input("Digite o número: "))
    lista.append(num)
    tupla = tuple(lista)

print(f"Listagem: {tupla}")
print(f"Menor número: {min(lista)}")
print(f"Maior número: {max(lista)}")

