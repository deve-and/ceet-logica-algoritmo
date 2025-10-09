"""
Função que simula uma conversa

    Crie uma função chamada responder(pergunta) que retorna uma resposta simples dependendo da pergunta (ex: se a pergunta for "Tudo bem?", retorna "Estou bem, obrigado!").
"""

def responder(pergunta):
    if pergunta.lower() == "tudo bem?":
        return "Estou bem, obrigado!"
    
print(responder("Tudo bem?"))