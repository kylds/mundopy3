from time import sleep 

def metade(valor):
    novo_valor = valor/2
    return novo_valor 

def dobro(valor):
    novo_valor = valor * 2
    return novo_valor 

def aumento(valor,porcento):
    i = (porcento/100) + 1 
    novo_valor = valor * i
    return novo_valor  

def redução(valor,porcento):
    k = (100 - porcento)/100
    novo_valor = valor * k
    return novo_valor

def moeda(valor,sit):
    if sit == True:
        n = str(valor)
        valor_str = n.replace('.',',') #tem que criar uma novo variável para receber o replace, não pode ser a msm que já recebeu a transformação float-str
        return valor_str
    else:
        sit=False 
        return valor  


def resumo(valor,porcento1,porcento2):
    print('-------------------------------------------------')
    print('RESUMO DO VALOR')
    print('-------------------------------------------------')
    sleep(0.5)
    print('Preço analisado: R${}'.format(moeda(valor,sit=True)), flush = True)
    print('Dobro do preço: R${}'.format(moeda(dobro(valor),sit=True),flush = True))
    print('Metade do preço: R${}'.format(moeda(metade(valor),sit=True),flsuh = True))
    print('35% de aumento: R${}'.format(moeda(aumento(valor,porcento1),sit=True), flush = True))
    print('22% de redução: R${}'.format(moeda(redução(valor,porcento2),sit=True),flush = True))
    print('-------------------------------------------------')
    return valor,porcento1,porcento2 