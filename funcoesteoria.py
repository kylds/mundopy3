# rotina é otimizar o processo, ou seja, se eu tenho que printar algo 6x eu posso fazer uma rotina para fazer uma vez
# se for um print: 
def mostraLinha():
    print('------------------------')

# voce repete apenas o def:
mostraLinha() # voce chama a função 
print('Sistema')
mostraLinha()
print('1 - Alunos  2- Educação  3- Comunicação')
mostraLinha()

# você pode definir parametros, ou seja chamar a mensagem:
def mensagem(msg):
    print('-----------')
    print(msg)
    print('------------')
mensagem('Sistema de Alunos')

def soma(a,b):
    soma = a + b 
    print('Soma: {} + {} = {}'.format(a,b,soma))

soma(4,3)
soma(10,10)
soma(8,2)


#desempacotar parâmetros: *
#colocar o * na frente significa que vai receber varios parâmetros, ou seja ários números e etc e quero desempacotar eles usando o for 

def contador(* núm):
    for valor in núm:
        print(núm)
        print('{}', end = ' '.format(valor)) # end pra quebrar a linha após o end 
print('FIM')

contador(2,1,7) #ele cria uma tupla 
contador(8,0)

#trabalhar com listas:

valores = [7,2,5,0,4] # ou seja o print vai ser o dobro desses valores da lista valores 
def dobra(lst):
    pos = 0 # posição inicial 0
    while pos < len(lst): # enquanto a pos for menor que o tamanho da lista 
        lst[pos] *= 2 #lst vai ser o dobro do pos 
        pos += 1 

dobra(valores)
print(valores)

end = '\n' # n quebrar a linha

#interactive help

help() #para obter essa ajuda vc faz isso, quando abre e fecha () apos um nome isso é uma função/método
# vc pode pedir ajuda do help em uma biblioteca, ele mostra tudo que tem e como usar 
# se vc digitar quit ele volta pra o terminal normal do py
help(print)

#docstring - uma string de documentação

def contador(i,f,p):
    """
    ---> Faça uma contagem na tela.
    ;para i: ínicio da contagem   
    ;pra f: fim da contagem
    ;para p: passo d acontagem 
    ;return: sem retorno
    """
    c = i #criar variavel para assumir o valor de i 
    while c <= f:
        print(f'{c}', end = '...')
        c += p
    print('FIM!')
#docstring começa dps da linha do def entre ""
help(contador)
contador(2,10,2)

#parametros opcionais 

def somar(a,b,c):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3,2,5)
soma(8,4) #falta c, se vc declarar assim o c não vai ter valo a não ser que use um parametro opcional que seria colocar c = 0

def somar(a,b,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

#escopo de variáveis 

def teste():
    x = 8 #escopo local, so vai funcionar dentre do def, o print fora do def não funciona
    print(f'Na função teste n vale {n}')

n = 2 #escopo global, até fora vai printar esse vale dentro do def
teste()

#se eu fizer isso vai deixa de ser utilizado o a global 

def teste(b):
    global a 
    a = 8
    b += 4 
    c = 2 
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5 
teste(a)
print(f'A fora vale {a}') #ele perde o valor 5, vai printar o 8 

#retornando valores 

def somar(a=9,b=0,c=0):
    s = a + b + c 
    print(f'A soma vale {s}')
    return s # vai fazer a chamada, somar, e depois vai retorna o s para a soma embaixo no resp

resp = soma(3,2,5)
resp1 = soma(2,2)
resp2 = soma(6)
print(f'Meus cálculos resultaram em {resp},{resp1} e {resp2}')