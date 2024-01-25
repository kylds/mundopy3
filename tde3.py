from time import sleep
from tde4 import *
from utilidadesCev.arquivo import *

#para importar um pacote de um módulo utilidadesCev.arquivo

arq = 'cursoemvideo.txt' #cria uma variável txt 

if not arquivoExiste(arq):
    criarArquivo(arq)


print('--------------------------------')
print('MENU PRINCIPAL')
print('--------------------------------')


while True:
    cadastro(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    print('--------------------------------')
    cad = int(input('Digite sua opção: '))
    print('--------------------------------')
    try:
        menu(cad)
        if cad > 3 or cad < 1:
            print('Erro! digite novamente')
        elif cad == 1:
            sleep(0.5)
            lerArquivo(arq)
            print('\n --------------------------------')
        elif cad == 2:
            print('--------------------------------')
            print('CADASTRO')
            print('--------------------------------')
            nome = str(input('Digite o nome: '))
            idade = int(input('Digite a idade: '))
            id = str(idade)
            if id.isalpha():
                print('Erro! digite novamente')
            cadastrar(arq,nome,id)
            print('\n --------------------------------')
        else:
            print('Programa finalizado! volte sempre')
            break
    except ValueError:
        print('Erro! digite novamente') 
    except TypeError:
        print('Erro! digite novamente')
    


