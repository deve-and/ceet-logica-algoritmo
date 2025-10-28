"""
Crie um programa que crie um arquivo chamado 'dados.txt' e escreva dentro dele a frase:
'Aprendendo manipulação de arquivos em Python!'. Use o comando with open() e o modo de
escrita ('w')
"""

with open("manipulacao-arquivos/ex01/dados.txt", "w") as dados:
    dados.write("Aprendendo manipulação de arquivos em Python!\n")
