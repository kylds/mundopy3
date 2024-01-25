listagem = ('Manteiga',10.0,
            'Pipos vitaminado', 12.50,
            'Sorvete Kibom', 15.0,
            'Feijão', 11.0, 
            'Batata frita', 21.0,
            'Nugets', 3.40, 
            'Refrigerante', 6.0, 
            'Biscoito recehado', 5.0)

print('*' * 10)
print("TABELA")
print('*' * 10)

for i in range(len(listagem)):
    if i % 2 == 0:
        print(f'{listagem[i]:.<30}', end = '')
    else:
        print(f' R${listagem[i]:.>7.3}')

