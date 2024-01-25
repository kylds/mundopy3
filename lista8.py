par = []
impar = []
for i in range(7):
    num = int(input(f"Digite o {i} valor: "))
    if num % 2!= 0:
        impar.append(num)
    else:
        par.append(num)



impar.sort()
par.sort()

print(f"Valores pares digitados: {par}")
print(f"Valores ímpares digitados: {impar}")