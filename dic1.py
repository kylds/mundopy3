for aluno in range(1):
    nome = str(input("Digite o nome do aluno: "))
    media = float(input("Digite a média do aluno: "))
    dados = dict()
    dados = {f'Aluno': nome, 'Média': media}
    if media >=7:
        print("O aluno foi aprovado")
    else:
        print("O aluno foi reprovado")

for k, v in dados.items():
    print('-'*10)
    print(f"{k} é {v}")