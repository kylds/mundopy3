
def notas(a,b,c,d,sit = 0):
    """
    ---> Informações:
    ;a,b,c,d: recebe as notas 
    ;sit: situação(boa,razoável,ruim)
    ;return: retornar as informações guardadas 
    """
    nota = []
    nota.append(a)
    nota.append(b)
    nota.append(c)
    nota.append(d)
    media = (a + b + c + d)/ 4 

    
    info = {'Quantidade de notas': len(nota), 
            'A maior nota': max(nota),
            'A menor nota': min(nota),
            'A média da turma': media}
    
    if sit == True:
        if media >= 7:
            info = {'Quantidade de notas': len(nota), 
            'A maior nota': max(nota),
            'A menor nota': min(nota),
            'A média da turma': media,
            'Situação': 'BOA'}
            print(info)
        elif 7 > media >= 5:
            info = {'Quantidade de notas': len(nota), 
            'A maior nota': max(nota),
            'A menor nota': min(nota),
            'A média da turma': media,
            'Situação': 'RAZOÁVEL'}
            print(info)
        else:
            info = {'Quantidade de notas': len(nota), 
            'A maior nota': max(nota),
            'A menor nota': min(nota),
            'A média da turma': media,
            'Situação': 'RUIM'}
            print(info)
    else:
        return info 
    


resp = notas(5.5,2.5,6.5,10,sit=True)