"""
Função que verifica se uma palavra começa com vogal
    Crie uma função chamada comeca_com_vogal(palavra) que retorna True se a primeira letra for uma vogal.
"""

def comeca_com_vogal(palavra):
    return palavra[0].lower() in 'aeiou'

print(comeca_com_vogal("anderson"))
print(comeca_com_vogal("texto"))

