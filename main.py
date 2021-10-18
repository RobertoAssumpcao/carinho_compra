"""
Criar uma lista de carinhos e criar um objeto para cada produto.
Criar funcao adicionar, excluir e editar
"""
# Declarando variaveis necessarias
fechamento_carinho = False
carrinho_pagamento = 0    

# imprimindo tabela
print("----------*Tabela preços*----------\ncodigo - produto - preço\n100 - Hot-dog - $1.20\n101 - Bauro - $1.30\n102 - Bauro com Ovo - $1.50\n")

#repeticao até o fechamento do carrinho
while fechamento_carinho == False:
    #Coletando codigo
    codigo_produto = int(input("Digite o codigo do produto:\n"))

    # verificando o que será acrescentado no carrinho
    if codigo_produto == 100:
        # Coletando quantidade de do produto
        quantidade_produto = int(input("Digite a quantidade:\n"))
        
        print("hot-dog adicionando com sucesso!")
        carrinho_pagamento = carrinho_pagamento +  (1.20 * quantidade_produto)
        print(f'O valor do carrinho está em ${carrinho_pagamento:.2f}')
        
    elif codigo_produto == 101:
        # Coletando quantidade de do produto
        quantidade_produto = int(input("Digite a quantidade:\n"))
        
        print("Bauru adicionando com sucesso!")
        carrinho_pagamento = carrinho_pagamento +  (1.30 * quantidade_produto)
        print(f'O valor do carrinho está em ${carrinho_pagamento:.2f}')
        
    elif codigo_produto == 102:
        # Coletando quantidade de do produto
        quantidade_produto = int(input("Digite a quantidade:\n"))
        
        print("Bauru com Ovo adicionando com sucesso!")
        carrinho_pagamento = carrinho_pagamento + (1.50 * quantidade_produto)
        print(f'O valor a ser pago está em ${carrinho_pagamento:.2f}')
        
    else:
        print("Codigo invalido")
    
    # verificando o fechamento do carrinho
    aux_fechamento_carrinho = input("Deseja fechar o carrinho ? Digite Y para fechar\n")   
    if aux_fechamento_carrinho == "Y":
        fechamento_carinho = True
    
print(f'O valor a ser pago é ${carrinho_pagamento:.2f}\n')