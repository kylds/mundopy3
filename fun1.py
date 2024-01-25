# área de um terreno 

def area(largura,comprimento):
    area = largura * comprimento
    print("A área de um terreno {}x{} é de {:.1f}m2 ".format(largura,comprimento,area)) 

print("Controle de terrenos")
print('------------------')

for i in range(1):
    largura = float(input("LARGURA(m): "))
    comprimento = float(input("COMPRIMENTO(m): "))
area(largura,comprimento)

