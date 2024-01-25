# parenteses 
lista = []

#toda string é uma lista

frase = str(input("Digite a expressão: ")).strip()
exp = [] #rastrear os parenteses 

for simb in frase: #itera sobre cada caracter da frase 
    if simb == '(': # se for esse ( add na lista exp para indicar que um parentese foi aberto da expressão
        exp.append('(')
    elif simb == ')':
        if len(exp) > 0:
            exp.pop() #ele verifica se há mais de um parenteses, para remover e fechar de maneira certa 
        else:
            exp.append(')')
if len(exp) == 0:
    print('A expressão está certa')
else: 
    print('A expressão está errada')




