"""
Função que junta nome e sobrenome

    Crie uma função chamada nome_completo(nome, sobrenome) que retorna o nome completo formatado.
"""

def nome_completo(nome, sobrenome):
    return  f'{nome} {sobrenome}'.upper()

print(nome_completo("Anderson", "gomes"))