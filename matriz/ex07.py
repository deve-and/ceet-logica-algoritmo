"""
Remova o primeiro número da segunda linha da matriz e exiba o
estado da matriz.
"""

from ex06 import matriz

matriz[1].pop(0)
if __name__ == "__main__":
    for row in matriz:
        for element in row:
            print(element, end=' ')
        print()