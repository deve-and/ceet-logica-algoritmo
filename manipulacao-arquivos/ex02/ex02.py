"""
    Faça um programa que abra o arquivo 'dados.txt' (criado no exercício anterior) e exiba seu conteúdo na tela.
"""

with open("manipulacao-arquivos/ex01/dados.txt", "r") as dados:
    conteudo = dados.read()
    print(conteudo)