"""
    Leia o arquivo 'frutas.txt' e mostre apenas as frutas que começam com a letra 'm'.
"""

with open('manipulacao-arquivos/ex06/frutas.txt', 'r') as frutas:
    listaFruta = frutas.readlines()
    for fruta in listaFruta:
        if fruta.startswith('M'):
         print(fruta.strip())    