lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input("Digite os números: "))
    add = str(input("Quer continuar? [S/N]: ")).upper()
    if add == 'N':
        break 
    else:
        lista.append(num)
        if num % 2 == 0:
            lista_par.append(num)
        else:
            lista_impar.append(num)

print(f"Lista: {lista}")
print(f"Números pares: {lista_par}")
print(f"Números ímpares: {lista_impar}")