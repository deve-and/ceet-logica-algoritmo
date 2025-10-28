"""
    Abra o arquivo 'frutas.txt' e mostre quantas linhas o arquivo possui (quantas frutas foram registradas).
"""

with open('manipulacao-arquivos/ex06/frutas.txt', 'r') as frutas:
    lista = frutas.readlines()
    print(len(lista))