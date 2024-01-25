
lista_id = []
soma_id = 0
from time import sleep 

pessoas = []

while True:
    nome = str(input("Digite o nome: "))
    sexo = str(input("Digite o sexo [F/M]: ")).upper()
    idade = int(input("Digite a idade: "))
    if sexo != 'F' and sexo != 'M':
        print("ERRO! Digite novamente")
        sexo = str(input("Digite o sexo [F/M]: ")).upper()
    lista_id.append(idade)
    pessoas.append({'Nome': nome,'Sexo': sexo, 'Idade': idade}) #método se usa ()   
    add = str(input("Deseja adicionar mais uma pessoa? [S/N]: ")).upper()
    if add != 'S' and add != 'N':
        print("ERRO! Digite novamente")
        add = str(input("Deseja adicionar mais uma pessoa? [S/N]: ")).upper()
    if add =='N':
        break  
lista_m = []
for k in range(len(pessoas)):
    soma_id += pessoas[k]['Idade']
    if pessoas[k]['Sexo'] == 'F':
        lista_m.append(pessoas[k]['Nome'])
media = soma_id/len(pessoas)

print('-' * 15)
sleep(0.5)
print(f"Total de pessoas cadastradas: {len(pessoas)}")
print(f"A média das idades é: {media}")
print(f"As mulheres presentes na lista são: {lista_m}")
print("Lista das pessoas com idade acima da média:")
for i in range(len(pessoas)):
      if pessoas[i]['Idade'] > media:
           print('{} é {}'.format(pessoas[i]['Nome'],pessoas[i]['Idade']))

       