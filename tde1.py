#reescrever a fufnção leiaInt()
from time import sleep
   
def leiaInt(num):
    while True:
        try:
            valor = int(input(num))
        except ValueError:
            print('Erro! digite novamente')
        except TypeError:
            print('Erro! digite novamente')
        else:
            return valor 

def leiaFloat(num):
        try:
            n = input(num)
            valor = str(n)
            while True:
                if '.' in valor:
                    return valor  
                else:
                    print('Erro! digite novamente')
                    n = input(num)
                    valor = str(n)
                    if valor.isalpha():
                        print('Erro! digite novamente')
                    elif '.' in valor:
                        return valor 
        except ValueError:
            print('Erro! digite novamente')
        except TypeError:
            print('Erro! digite novamente') 
        
print('-------------------------')
numero = leiaInt('Digite um número inteiro: ')
numeral = leiaFloat('Digite um número real: ')
print('-------------------------')
sleep(0.5)
print('O número inteiro digitado é {} e o real é {}'.format(numero,numeral))