import os

#Dados inicial (usada apenas se o arquivo não existir)
dados_iniciais = [
    [1, "Arroz", 10.50, 25],
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

#Variável para facilitar a troca futura do nome do arquivo, caso necessário
ARQUIVO_ESTOQUE = "dados/estoque.txt"

estoque = []
ultimo_id_produto = 0

#Funções usadas no setor ESTOQUE 

#Função para salvar o estoque no arquivo
def carregar_estoque():
    global estoque, ultimo_id_produto

    if os.path.exists(ARQUIVO_ESTOQUE):
        estoque.clear()
        with open(ARQUIVO_ESTOQUE, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if linha == "":
                    continue
                partes = linha.split(" ; ")
                id_p    = int(partes[0])
                nome    = partes[1]
                preco   = float(partes[2])
                qtd     = int(partes[3])
                estoque.append([id_p, nome, preco, qtd])
        if estoque:
            ultimo_id_produto = max(p[0] for p in estoque)
    else:
        estoque.clear()
        estoque.extend([list(p) for p in dados_iniciais])
        ultimo_id_produto = 10
        salvar_estoque()


#Função para salvar o estoque no arquivo
def salvar_estoque():
    os.makedirs("dados", exist_ok=True)
    with open(ARQUIVO_ESTOQUE, "w", encoding="utf-8") as f:
        for produto in estoque:
            linha = f"{produto[0]} ; {produto[1]} ; {produto[2]} ; {produto[3]}\n"
            f.write(linha)

#Carrega o estoque ao executar o codigo
carregar_estoque()


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
    salvar_estoque()
    
    print("Produto cadastrado com sucesso!")


#Função para atualizar as informações de um produto existente
def atualizar_produto_completo():
    
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
    salvar_estoque()
    
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
    salvar_estoque()
    
    print("Estoque atualizado com sucesso!")

#Função para atualizar o preço de um produto
def atualizar_preco():
    print("=" * 49)
    print("===========     ATUALIZAR PREÇO     ===========")
    print("=" * 49)
    
    ver_lista_produtos()
    
    id_produto = int(input("Digite o ID do produto para atualizar o preço: "))
    produto = buscar_produto(id_produto)
    
    if produto is None:
        print("ERRO: Produto não encontrado.")
        return
    
    print(f"Nome: {produto[1]}")
    print(f"Preço atual: R${produto[2]:.2f}")
    
    novo_preco = float(input("Digite o novo preço do produto: R$"))
    
    produto[2] = novo_preco
    salvar_estoque()
    
    print("Preço atualizado com sucesso!")


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
    salvar_estoque()
    
    print("Produto excluído com sucesso!")


#Menu para escolher qual tipo de atualização deseja fazer em um produto existente
def menu_atualizacao_produto():
    while True:
        print("=" * 50)
        print("===========     ATUALIZAR PRODUTO     ===========")
        print("=" * 50)

        print("1 - Atualizar nome, preço e quantidade do produto")
        print("2 - Atualizar apenas a quantidade do produto")
        print("3 - Atualizar apenas o preço do produto")
        print("4 - Atualizar apenas o nome do produto")
        print("0 - Voltar ao menu anterior")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                atualizar_produto_completo()
            case "2":
                atualizar_estoque()
            case "3":
                atualizar_preco()
            case "4":
                atualizar_nome()
            case "0":
                break
            case _:
                print("Opção inválida. Tente novamente.")


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
        
        match opcao:
            case "1":
                listar_produtos()
            case "2":
                cadastrar_produto()
            case "3":
                atualizar_produto()
            case "4":
                atualizar_estoque()
            case "5":
                excluir_produto()
            case "0":
                print("Voltando ao menu principal.")
                break
            case _:
                print("Opção inválida. Tente novamente.")