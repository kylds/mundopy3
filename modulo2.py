#aprimorando o módulo moeda.py
import moeda 

preco = float(input('Digite o preço: R$ '))
print('A metade de R${} é R${}'.format(moeda.moeda(preco,sit=True),moeda.moeda(moeda.metade(preco),sit=True)))
print('O dobro de R${} é R${}'.format(moeda.moeda(preco,sit=True),moeda.moeda(moeda.dobro(preco),sit=True)))
print('Aumentando 10%, temos R${}'.format(moeda.moeda(moeda.aumento(preco,10),sit=True)))
print('Reduzindo 13%, temos R${}'.format(moeda.moeda(moeda.redução(preco,13),sit=True)))
