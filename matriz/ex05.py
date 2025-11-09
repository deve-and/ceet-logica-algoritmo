"""
Remova a última linha da matriz (que você adicionou na questão
anterior) e exiba novamente o conteúdo da matriz.
"""

from ex04 import matriz

del matriz[3]
if __name__ == "__main__":
    for row in matriz:
        for element in row:
            print(element, end=' ')
        print()