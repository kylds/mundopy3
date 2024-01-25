from time import sleep 
from math import factorial 
def fatorial(n):
    fat = factorial(n)
    for i in range(n,0,-1): 
        print('{}'.format(i), end = '', flush = True)
        if i > 1:
            sleep(0.5) # tem que ser maior que 1, pq quando chegar a 0, o elemento 0 não vai ser printado e sim o print do fat
            print('x', end = '', flush = True)
        else:
            print('= {}'.format(fat), end = '', flush = True)
    return fat 