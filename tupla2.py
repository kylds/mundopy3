#brasileirão
print("-="*20)
print("BRASILEIRÃO")
print("-="*20)

#Na questão pede a posição da chapecoense porém o time não estava no top 20 times do brasileirão 2023

print("Para para o programa digite -1")

while True:
    tupla = ('Palmeiras', 'Botafogo', 'Grêmio', 'Bragantino', 'Atlético-MG',
             'Flamengo', 'Athletico-PR', 'Fluminense', 'Cuiabá',
             'São Paulo', 'Corinthians', 'Fortaleza', 'Internacional', 
             'Santos', 'Vasco da Gama', 'Bahia', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')
    escolha = int(input("1 - Cinco primeiros colocados \n 2 - Quatro últimos colocados \n 3 - Lista em ordem alfabética \n 4 - Posição do Vasco da Gama \n Digite: "))
    if escolha == -1:
        break
    if escolha > 4 or escolha < -1:
        print("Número inválido")
    else:
        if escolha == 1:
            print(tupla[:5])
        elif escolha == 2:
            print(tupla[16:])
        elif escolha == 3:
            print(sorted(tupla))
        elif escolha == 4:
            for vasco in range(1):
                v = tupla.index('Vasco da Gama')
                print(f"A posição do time Vasco da Gama é {v} posição")