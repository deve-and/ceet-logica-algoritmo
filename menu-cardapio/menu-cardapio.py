
def exibeCardapio(): # Exibe o menu
    print("""
    ------------ CARDÁPIO ------------
    1 - Hamburguer ---------- R$ 15,00
    2 - Pizza      ---------- R$ 20,00
    3 - Refrigerante -------- R$ 5,00
    4 - Sobremesa  ---------- R$ 10,00
    0 - ----- Finalizar Pedido -------
""")
    
itensCardapio = {
    1: ("Hamburguer", 15.0),
    2: ("Pizza", 20.0),
    3: ("Refrigerante", 5.00),
    4: ("Sobremesa", 10.0),
}

pedido = None
somaTotal = 0

while pedido != 0:
    exibeCardapio()
    pedido = int(input("Digite o número do item desejado: "))
    if pedido in itensCardapio:
        nome, preco = itensCardapio[pedido]
        somaTotal += preco
    elif pedido == 0:
        print('Pedido finalizado.\n')
        print(f'Soma total do pedido: R$ {somaTotal:.2f}')
        
    else:
        print("Opção inválida. Tente novamente.\n")


