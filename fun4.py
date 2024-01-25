#maior valor 
#VOU OLHAR A RESOLUÇÃO!


from time import sleep 



# desempacotando
def maior(* num):
    cont = maior = 0
    print('Analisando os valores')
    for valor in num: #num é considerado uma tupla, ent tem que comparar valor com maior 
        cont += 1
        if valor > maior:
            maior = valor 
    sleep(0.5)
    print('{} Foram mostrados {} valores'.format(num,cont), flush = True)
    print('O maior valor foi {}'.format(maior))

    
maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6,0)
maior(0)