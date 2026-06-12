#Matriz para armazenar os produtos em estoque
estoque = [
    [1, "Arroz", 10.50, 25], #ID, nome, preço, quantidade
    [2, "Feijão", 8.99, 18],
    [3, "Macarrão", 4.50, 34],
    [4, "Leite", 6.99, 25],
    [5, "Café", 12.00, 14],
    [6, "Açúcar", 3.50, 30],
    [7, "Bolacha", 2.00, 50],
    [8, "Óleo", 7.50, 20],
    [9, "Sal", 1.99, 30],
    [10, "Pão", 1.00, 50]
]

ultimo_id_produto = 10

#Funções usadas no setor ESTOQUE

#Função para buscar um produto pelo ID
def buscar_produto(id_produto):
    for produto in estoque:
        if produto[0] == id_produto:
            return produto
    
    return None

#Função para listar os produtos em estoque
def listar_produtos():
    
    print("=" * 49)
    print("================     ESTOQUE     ================")
    print("=" * 49)
    
    for produto in estoque:
        print(f"ID: {produto[0]} | Nome: {produto[1]} | Preço: R${produto[2]:.2f} | Quantidade: {produto[3]}")

#Escolher se deseja ver a lista de produtos
def ver_lista_produtos():
    ver_lista = int(input("Deseja ver a lista de produtos antes? (1 - Sim, 0 - Não): "))
    if ver_lista == 1:
        listar_produtos()

#Função para cadastrar um novo produto no estoque
def cadastrar_produto():
    
    global ultimo_id_produto
    
    print("=" * 49)
    print("===========     CADASTRAR PRODUTO     ===========") 
    print("=" * 49)

    nome_produto = input("Digite o nome do produto: ")
    
    if nome_produto == "":
        print("ERRO: Nome inválido!")
        return
    
    preco = float(input("Digite o preço do produto: R$"))
    quantidade = int(input("Digite a quantidade do produto: "))
    
    ultimo_id_produto += 1
    id_produto = ultimo_id_produto
    
    estoque.append([id_produto, nome_produto, preco, quantidade])
    
    print("Produto cadastrado com sucesso!")

#Função para atualizar as informações de um produto existente
def atualizar_produto():
    
    print("=" * 49)
    print("===========     ATUALIZAR PRODUTO     ===========")
    print("=" * 49)
    
    ver_lista_produtos()
    
    id_produto = int(input("Digite o ID do produto a ser atualizado: "))
    produto = buscar_produto(id_produto)
    
    if produto is None:
        print("ERRO: Produto não encontrado.")
        return
    
    novo_nome = input("Digite o novo nome do produto: ")
    if novo_nome == "":
        print("ERRO: Nome inválido! Produto não foi atualizado.")
        return
    
    produto[1] = novo_nome
    produto[2] = float(input("Digite o novo preço do produto: R$"))
    produto[3] = int(input("Digite a nova quantidade do produto: "))
    
    print("Produto atualizado com sucesso!")    

#Função para atualizar a quantidade em estoque de um produto existente
def atualizar_estoque():
    
    print("=" * 49)
    print("===========     ATUALIZAR ESTOQUE     ===========")
    print("=" * 49)
    
    ver_lista_produtos()
    
    id_produto = int(input("Digite o ID do produto para atualizar o estoque: "))
    produto = buscar_produto(id_produto)
    
    if produto is None:
        print("ERRO: Produto não encontrado.")
        return
    
    print(f"Nome: {produto[1]}")
    print(f"Quantidade atual: {produto[3]}")
    
    nova_quantidade = int(input("Digite a nova quantidade do produto: "))
    
    produto[3] = nova_quantidade
    
    print("Estoque atualizado com sucesso!")

#Função para excluir um produto do estoque, verificando se ele possui vendas registradas
def excluir_produto():
    from vendas import vendas
    
    print("=" * 50)
    print("============     EXCLUIR PRODUTO      ============")
    print("=" * 50)
    
    ver_lista_produtos()
    
    id_produto = int(input("Digite o ID do produto a ser excluído: "))
    produto = buscar_produto(id_produto)
    
    if produto is None:
        print("ERRO: Produto não encontrado.")
        return
    
    for venda in vendas:
        if venda[1] == id_produto:
            print("ERRO: Produto não pode ser excluído.")
            print("Este produto possui vendas registradas.")
            return
    
    estoque.remove(produto)
    
    print("Produto excluído com sucesso!")

#Função para exibir o menu de opções do setor ESTOQUE
def menu_estoque():
    while True:
        print("=" * 49)
        print("============     MENU DE ESTOQUE     ============")
        print("=" * 49)
        
        print("1 - Listar produtos")
        print("2 - Cadastrar produto")
        print("3 - Atualizar produto")
        print("4 - Atualizar estoque")
        print("5 - Excluir produto")
        print("0 - Voltar ao menu principal")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            listar_produtos()
            
        elif opcao == "2":
            cadastrar_produto()
            
        elif opcao == "3":
            atualizar_produto()
            
        elif opcao == "4":
            atualizar_estoque()
            
        elif opcao == "5":
            excluir_produto()
            
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")

