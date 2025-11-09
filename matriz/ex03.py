"""
Altere o valor do elemento da posição [1][2] (linha 2, coluna 3) da
matriz para o número 99. Mostre a matriz atualizada.
"""

from ex01 import matriz

matriz[1][2] = 99
for row in matriz:
    for element in row:
        print(element, end=' ')
    print()