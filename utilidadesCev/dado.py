def leiaDinheiro(valor):
    while True:
        dinheiro = input(valor) #2
        if dinheiro.isnumeric(): #vai ler a/b/c/2/3/i8/o9 como strings por isso que é preciso converter pra ele virar um float se não o programa não vai rodar 
            return float(dinheiro) 
        else:
            print('ERRO! digite novamente')

