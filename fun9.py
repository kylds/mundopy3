#funcionar como um input 

def leiaInt(pergunta):
    while True:
        entrada = input(pergunta) #vai ler a variavel pergunta
        if entrada.isnumeric(): #vai ver se todos os elementos são numéricos
            return entrada 
        else:
            print('Erro! Digite um número')
num = leiaInt('Digite um número: ')
print('Você digitou o número {}'.format(num))