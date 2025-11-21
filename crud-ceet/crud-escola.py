# Lista que receberá os dados dos alunos
listaAlunos = []

# menu de opões do sistema
menu = {1: 'Cadastrar Aluno',
        2: 'Listar Alunos',
        3: 'Atualizar Aluno',
        4: 'Excluir Aluno',
        5: 'Sair do Programa'}


# CREATE
def cadastrarAluno():
    # Solicita os dados do aluno
    nome = input('Nome completo: ')
    notaFinal = float(input('Nota final: '))
    totalFaltas = int(input('Total de faltas: '))

    # Condição para avaliar a situação do aluno
    situacao = ' '
    media = notaFinal
    if (media >= 60 and media <= 100) and totalFaltas <= 30:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'

    # Estrutura da lista dos dados do aluno
    aluno = {
        'nome': nome,
        'nota': notaFinal,
        'faltas': totalFaltas,
        'situacao': situacao
    }

    # Adiciona as informações do aluno na lista de alunos
    listaAlunos.append(aluno)

    # Cria arquivo de texto para visualiar os dados dos alunos
    with open('crud-ceet/alunos.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome} - Nota: {notaFinal} - Faltas: {totalFaltas} - Situação: {situacao}\n')

# READ
def listarAlunos():
    # Imprime o/os alunos
    if len(listaAlunos) == 0:
        print('Nenhum aluno cadastrado')
    else:
        print('\n--- Alunos Cadastrados ---')
        for aluno in listaAlunos:
            print(f"Nome Completo: {aluno['nome']}")
            print(f"Nota Final: {aluno['nota']}")
            print(f"Total de Faltas: {aluno['faltas']}")
            print(f"Situação: {aluno['situacao']}")
            print("-" * 25)
            print()


