#modularização é o ato de construir módulos 

#fatorial 

import uteis
#todo arquivo .py pode ser um módulo       

num = int(input("Digite um número: "))
fat  = uteis.factorial(num) #importar o factorial de uteis.py
print('\nO fatorial do número {} é {}'.format(num,fat))

#pacotes
#cria uma pasta uteis e dentro dela cria um módulo do que você quer(datas,cores,numeros)
#pacotes são para exercícios muito grandes
#dentro de cada pacotes tem que ter um arquivo init (__init__.py)

