from time import sleep

print('-' * 20)
print("Informações trabalhistas")
print('-' * 20)

lista_nasc = []
lista_nome = []


while True:
    nome = str(input("Digite o nome: "))
    nascimento = int(input("Digite o ano de nascimento: "))
    cart_trabalho = int(input("Digite o número da carteira de trabalho [Não pode conter zero]: "))
    ano_cont = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite o salário: "))
    add = str(input("Deseja adionar algum trabalhador? [S/N]: ")).upper()
    lista_nasc.append(nascimento) 
    for i in range(len(lista_nasc)):
        idade = 2024 - lista_nasc[i] #tem que colocar o cont para identificar a ordem das pessoas 
        dif = 2024 - ano_cont
        if dif < 35:
            trab = 35 - dif 
            aposentadoria = trab + idade 
        else:
            aposentadoria = idade
    pessoas = {f"Nome": nome, "idade": nascimento,"CTPS": cart_trabalho, "Contratação": ano_cont, "Salário": salario, "Aposentadoria": aposentadoria}
    print('-' * 25)
    sleep(0.5)
    for k, v in pessoas.items():
        print("{} é {}".format(k,v))
    if add == 'N':
        break  

# da biblioteca datetime pode-se fazer datetime.now().year-nas descobrir a diferença