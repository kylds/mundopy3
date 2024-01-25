def escreva(msg):
    print('-'*len(msg))
    print(msg)
    print('-'*len(msg)) #com caracter o len pode ser usado, já com int e float não
escreva('Olá, mundo!')
escreva('Kailany')
escreva('Curso em vídeo: Python')

# posso criar tb uma variável tam para medir a msg 
# tam = len(msg) se eu quiser fazer um pouco maior tam = len(msg) + 4 