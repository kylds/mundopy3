#tratamento de erros 

#primt(x) - erro de sintaxe

# print(x) - Name error, por que o x não foi definido 

# n = int(input('Número: ')) - Value error, se não receber um valor int (float,str,...)

# a = int(input('Numerador: ')) 
# b = int(input('Denominador: '))
# r = a/b - Zero Division error, se b = 0

# r = 2/ '2' - Type error, o '2' não é número 

# lst = [3,6,4]
#print(lst[3]) - Index error, 3 é índice e ele não existe

# try - tentar/ execept - deu errado/ else - deu certo/ finally - certo/errado vai acontecer independete do resultado

# from naoseeioq import naosei * - importa tudo de naoseioq

try:
    a = int(input('Numerador: '))
    b = int(input('Digite o Denominador: '))
    r = a/b 
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados digitados')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero')
except Exception as erro:
    print('O erro encontrado foi {}'.format(erro.__cause__))
else:
    print('O resultado é {}'.format(r))
finally:
    print('Finalizado! volte sempre')

# para mostrar o tipo de erro pode colocar erro.__class__ no lugar do r no format
#todo try pode ter mais de um excepts 
    
#try:
#    valor = float(input(num))
#except ValueError:
#    print('Erro! digite novamente')
#    valor = float(input(num)) - não precisa digitar isso aqui de novo, pois ele ja repete normalmente
#except TypeError:
#    print('Erro! digite novamente')
#    valor = float(input(num))
#else:
#    print('O resultado é {}'.format(valor))
#    return valor  