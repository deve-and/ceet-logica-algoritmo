"""
    Crie uma lista com 5 frutas e grave cada fruta em uma linha dentro de um arquivo chamado 'frutas.txt'.
"""

with open('manipulacao-arquivos/ex06/frutas.txt', 'a') as frutas:
    frutas.write('Abacaxi\n')
    frutas.write('Banana\n')
    frutas.write('Maçã\n')
    frutas.write('Manga\n')
    frutas.write('Caju\n')
    