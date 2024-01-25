

def voto(* nasc):
    ano_atual = 2024
    for idade in nasc:
        if ano_atual - idade >= 18:
            print('A pessoa possui {} anos, então o voto é obrigatório'.format(ano_atual - idade))
        elif 18 > ano_atual - idade >= 16:
            print('A pessoa possui {} anos, então o voto é opcional'.format(ano_atual - idade))
        else:
            print('A pessoa possui {} anos, então o voto é negado'.format(ano_atual - idade))

print('-----------------------------------------')
nasc = int(input('Digite sua data de nascimento: '))
print('-----------------------------------------')

voto(nasc)

# from date time import date 
# atual = date.today().year - pegar o ano atual 