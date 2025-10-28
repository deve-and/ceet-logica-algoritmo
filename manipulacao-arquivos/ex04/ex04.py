"""
    Abra o arquivo 'alunos.txt' e leia seu conteúdo linha por linha, mostrando o nome de cada aluno com a mensagem: 'Aluno: [nome]
"""

with open ("manipulacao-arquivos/ex03/alunos.txt", "r") as alunos:
    linhas = alunos.readlines()
    for linha in linhas:
        print(f'Aluno: {linha.strip()}')