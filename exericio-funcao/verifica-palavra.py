"""
Função que verifica se uma palavra está na frase

    Crie uma função chamada palavra_na_frase(palavra, frase) que retorna True se a palavra estiver na frase.
"""

def palavra_na_frase(palavra, frase):
    palavraFormatada = palavra.lower()
    fraseFormatada = frase.lower()
    if palavraFormatada in fraseFormatada:
        return True
    else:
        return False

print(palavra_na_frase("Vasco", "Escola Vasco Coutinho"))