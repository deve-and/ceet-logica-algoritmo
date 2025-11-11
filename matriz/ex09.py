"""
Suponha que sua matriz tenha repetições de um número, por exemplo, o número 5. Conte quantas vezes o número 5 aparece na matriz e
exiba esse total.
"""

from ex07 import matriz

total = 0
for linha in matriz:
    for elemento in linha:
        if elemento == 5:
            total += 1

print(f'O total de números 5 na lista é: {total}')
