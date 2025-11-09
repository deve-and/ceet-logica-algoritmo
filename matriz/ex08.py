"""
Mostre apenas os números da diagonal principal da sua matriz (ou
seja, elementos onde índice da linha é igual ao índice da coluna: [0][0],
[1][1], etc.).
"""

from ex07 import matriz

for indLinha in range(len(matriz)):
    for indElemento in range(len(matriz[indLinha])):
        if indLinha == indElemento:
            print(matriz[indLinha][indElemento])