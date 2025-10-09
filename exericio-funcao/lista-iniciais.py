""""
Função que retorna a primeira letra de cada nome

    Crie uma função chamada iniciais(lista_de_nomes) que retorna uma lista com as letras iniciais de cada nome.
"""
lista_de_nomes = ['Anderson', 'Gomes', 'da', 'Silva']

def iniciais(lista_de_nomes):
    iniciais = []
    for nome in lista_de_nomes:
        iniciais.append(nome[0])
    return iniciais

print(iniciais(lista_de_nomes))