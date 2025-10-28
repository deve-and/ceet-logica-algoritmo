"""
    Crie um programa que leia o conteúdo de 'frutas.txt' e grave as mesmas linhas em um novo arquivo chamado 'frutas_copia.txt'.
"""

with open('manipulacao-arquivos/ex06/frutas.txt', 'r') as frutas:
    listaFrutas = frutas.read()

with open('manipulacao-arquivos/ex09/frutas_copia.txt', 'w') as frutasCopia:
    frutasCopia.write(listaFrutas)