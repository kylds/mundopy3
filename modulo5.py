#aprimorando o módulo moeda.py
from utilidadesCev.moeda import *
from utilidadesCev.dado import * 

preco = leiaDinheiro('Digite o preço: R$') #qualquer módulo, pacote que chamar de outro lugar precisa chamar o nome dele . a função que ele quer, exemplo: dado.leiaDinheiro()
resumo(preco,35,22)