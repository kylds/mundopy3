def arquivoExiste(nome): #verifica se o arquivo existe
    try:
        a = open(nome,'rt') #tentar abrir o arquivo para leitura('rt - readtext')
        a.close() #fechar o arquivo
    except FileNotFoundError:
        return False 
    else:
        return True 

def criarArquivo(nome): #cria o arquivo 
    try:
        a = open(nome,'wt+') #wt+ - write text, o + é que se por acaso o arquivo não existe ele cria um
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('O arquivo {} está no sistema'.format(nome))

def lerArquivo(nome):
    try:
        a = open(nome,'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        print('--------------------------------')
        print('PESSOAS CADASTRADAS')
        print('--------------------------------')
        for linha in a:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n',' ')
            print(f'{dado[0]:<30}{dado[1]:>3}anos')
        print(a.read()) #readlines é para ler as linhas do arquivo, read - para ler 

def cadastrar(arq,nome = 'desconhecido',idade = 0):
    try:
        a = open(arq, 'at') #at funciona como um append de lista 
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write('{}: {} \n'.format(nome,idade)) #write - escrever no arquivo esses dados
        except:
            print('Houve um erro para abir o arquivo')
        else:
            print('Novo registro de {} adicionado'.format(nome))
            a.close()