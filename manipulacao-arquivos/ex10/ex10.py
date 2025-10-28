"""
    Crie dois arquivos: 'nomes.txt' com três nomes e 'idades.txt' com três idades correspondentes. Depois, leia os dois arquivos e crie um terceiro arquivo chamado 'pessoas.txt', no formato: Nome: João - Idade: 25.
"""

with open('manipulacao-arquivos/ex10/nomes.txt', 'a') as arqNomes:
    arqNomes.write('Anderson\n')
    arqNomes.write('Evany\n')
    arqNomes.write('Barbara\n')

with open('manipulacao-arquivos/ex10/idades.txt', 'a') as arqIdades:
    arqIdades.write('32\n')
    arqIdades.write('56\n')
    arqIdades.write('27\n')

with open('manipulacao-arquivos/ex10/nomes.txt', 'r') as arqNomes:
    nomes = arqNomes.readlines()

with open('manipulacao-arquivos/ex10/idades.txt', 'r') as arqIdades:
    idades = arqIdades.readlines()

with open('manipulacao-arquivos/ex10/pessoas.txt', 'w') as arqPessoas:
    for cont in range(len(nomes)):
        nome = nomes[cont].strip()
        idade = idades[cont].strip()
    
        linha = f'Nome: {nome} - Idade: {idade}\n'
        arqPessoas.write(linha)
    


