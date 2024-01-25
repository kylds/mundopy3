# contador 

from time import sleep 

def contador(ínicio,fim,passo):
     if passo < 0:
          passo *= -1 #para mudar o sinal de - para +
     if passo == 0:
          passo = 1 
     print('\n Contagem de {} até {}, de {} em {}'.format(ínicio,fim,passo,passo)) # o print tem que ser aqui para aparecer antes do print do código 
     print('------------------------------------')
     if ínicio < fim:
          cont = ínicio 
          while cont <= fim:
              print('{}'.format(cont), end = '', flush=True) # flush - pra fazer a contagem número por número devagar 
              sleep(0.5)
              cont += passo
     else:
          cont = ínicio
          while cont >= fim:
               print(' {}'.format(cont),end = '', flush=True)
               sleep(0.5)
               cont -= passo 
     

contador(1,10,1)
contador(10,0,2)
print('Agora é sua vez de personalizar a contagem!')
sleep(0.5)
inicio = int(input('Ínicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio,fim,passo)