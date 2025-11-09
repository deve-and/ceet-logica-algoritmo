"""
Crie uma matriz 3x3 com números inteiros à sua escolha e exiba todos
os elementos na tela.
Exemplo de saída:
1 2 3
4 5 6
7 8 9
"""

matriz = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
        ]

if __name__ == "__main__":
        for row in matriz:
                for elem in row:
                        print(elem, end=' ')
                print()