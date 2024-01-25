import moeda

preco = float(input('Digite o preço: R$ '))
print('A metade de {} é {}'.format(preco,moeda.metade(preco)))
print('O dobro de {} é {}'.format(preco,moeda.dobro(preco)))
print('Aumentando 10%, temos {}'.format(moeda.aumento(preco,10)))
print('Reduzindo 13%, temos {}'.format(moeda.redução(preco,13)))

#quando chamar o modulo, eles tem que ser chamados pelas def's