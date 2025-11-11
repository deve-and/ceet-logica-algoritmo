"""
Imprima apenas os números maiores que 5 da sua matriz, em forma de lista simples (ex.: [7, 9, 100]).
"""

from ex07 import matriz

maiores = []

for linha  in matriz:
    for elemento in linha:
        if elemento > 5:
            maiores.append(elemento)

print(maiores)