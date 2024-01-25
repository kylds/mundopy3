# dicionarios em py - {}
# lista - [] / tupla ()

dados = dict()
dados = {'nome':'Pedro','idade':'25'}
print(dados['nome'])
print(dados['idade'])

filme = { 'título':'Star Wars',
        'ano':'1997',
}
print(filme.values()) #printa todos valores (star wars,1997)
print(filme.keys()) #printa a parte de baixo(título,ano) 
print(filme.items()) #printa tudo 

for k, v in filme.items():
    print(f"{k} é {v}")  #ele funciona igual ao enumerate 
    # k de keys e v de values 
    # vai printar: O título é Star Wars / O ano é 1997 

from operator import itemgetter #ordenar o dicionario    
ranking = sorted(filme.items((), key = itemgetter(1), reverse = True)) #se for parte 0 vai ordenar em forma e chave, se for parte 1 vai ordenar em forma de valor
# o reverse é para o primeiro lugar ser o maior elemento   

#criar uma lista aonde cada elemento tem um dicionario dentro
#lista indentificada por números, dicionario por palavras,números(chaves)

for k in filme.keys():
    print(k) 
    
for k in filme.values():
    print(k)

for k, v in filme.intems():
    print(f'{k} = {v}')

# para deletar - del['título']