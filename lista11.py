nome_lista = []
notas_1 = []
notas_2 = []
medias = []

while True:
    nome = str(input("Digite o nome do aluno: "))
    nota_1 = float(input("Digite a primeira nota: "))
    nota_2 = float(input("Digite a segunda nota: "))
    add = str(input("Deseja adicionar mais um aluno? [S/N]: ")).upper()
    nome_lista.append(nome)
    notas_1.append(nota_1)
    notas_2.append(nota_2)
    media = (nota_1 + nota_2)/2
    medias.append(media)
    if add == 'N':
        break    
    

for boletim in range(len(nome_lista)):
    print("**** BOLETIM ****")
    print(f'{boletim} - {nome_lista[boletim]} ------ {notas_1[boletim]}, {notas_2[boletim]} ---- Média: {medias[boletim]}')
    print("**** ****")
    #vai printar o nome de cada índice indicado pela variável boletim

while True:
    busca_nota = int(input("Digite o índice se quiser saber a nota de algum aluno, se não digite 999: "))
    if busca_nota == 999:
        print("FINALIZADO")
        break 
    else:
        if busca_nota < len(nome_lista):
            print(f"Aluno: {nome_lista[busca_nota]} --- notas: {notas_1[busca_nota]}, {notas_2[busca_nota]}")
        else:
            print("Inválido")
    

    