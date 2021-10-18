# Declarando variaveis necessarias
fechamento_carinho = False
carrinho_pagamento = 0

#repeticao até o fechamento do carrinho
while fechamento_carinho == False:
    #Coletando codigo e quantidade
    codigo_produto = int(input("Digite o codigo do produto\n"))
    quantidade_produto = int(input("Digite a quantidade\n"))

    # verificando o que será acrescentado no carrinho
    if codigo_produto == 100:
        print("hot-dog")
        carrinho_pagamento = carrinho_pagamento +  (1.20 * quantidade_produto)
    elif codigo_produto == 101:
        print("Bauru")
        carrinho_pagamento = carrinho_pagamento +  (1.30 * quantidade_produto)
    elif codigo_produto == 102:
        print("Bauru com Ovo")
        carrinho_pagamento = carrinho_pagamento + (1.50 * quantidade_produto)
    
    # verificando o fechamento do carrinho
    aux_fechamento_carrinho = input("Deseja fechar o carrinho, digite Y para fechar ?\n")   
    if aux_fechamento_carrinho == "Y":
        fechamento_carinho = True
    
print(carrinho_pagamento)