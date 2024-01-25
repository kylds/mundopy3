# tupla é com ()
# sorted vai organizar a tupla 
# a soma em tupla junta as tuplas 
# para não usar format toda vez pode colocar f no começo da frase 
# tupla é imutável



while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if num>20 or num<0:
        print("Número inválido")
        break 
    else:
       tupla = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')
       print(f"Você digitou o número {tupla[num]}")
       #para acessar o numero extenso procura o num dentro da lista 

