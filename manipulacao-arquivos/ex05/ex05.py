"""
    Faça um programa que adicione (sem apagar o conteúdo anterior) uma nova linha com outro nome ao arquivo 'alunos.txt'. (Dica: use o modo 'a' de append
"""

with open("manipulacao-arquivos/ex03/alunos.txt", "a") as alunos:
    alunos.write("Anderson\n")
