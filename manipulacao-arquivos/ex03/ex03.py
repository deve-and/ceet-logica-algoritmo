"""
    Crie um programa que escreva três linhas em um arquivo chamado 'alunos.txt'. Cada linha deve conter o nome de um aluno.
"""

with open("manipulacao-arquivos/ex03/alunos.txt", "w") as alunos:
    alunos.write("Ana\n")
    alunos.write("João\n")
    alunos.write("Maria\n")