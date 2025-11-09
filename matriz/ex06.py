"""
Adicione um novo número à primeira linha da matriz. O número é
100. Exiba a matriz após a alteração.
"""

from ex05 import matriz

novoElemento = 100
matriz[0].append(novoElemento)

if __name__ == "__main__":
    for row in matriz:
        for element in row:
            print(element, end=' ')
        print()