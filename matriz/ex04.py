"""
Adicione uma nova linha [10, 11, 12] à matriz já existente e exiba a
matriz completa.
"""

from ex03 import matriz

novaLinha = [10, 11, 12]
matriz.append(novaLinha)

if __name__ == "__main__":
    for row in matriz:
        for element in row:
            print(element, end=' ')
        print()
