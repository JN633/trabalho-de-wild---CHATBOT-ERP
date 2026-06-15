from estoque import estoque, listar_produtos, buscar_produto, ver_lista_produtos

#Matriz para armazenar as vendas
vendas = [  
    [1, 1, 2, 10.50, 21.00], #ID Venda, ID produto, quantidade, preço Unitário, Valor Total
    [1, 2, 1, 8.99, 8.99],
    [2, 5, 1, 12.00, 12.00],
    [3, 3, 2, 4.50, 9.00],
    [4, 4, 3, 6.99, 20.97],
    [5, 8, 1, 7.50, 7.50],
    [6, 9, 4, 1.99, 7.96],
    [7, 10, 2, 1.00, 2.00],
    [8, 6, 2, 3.50, 7.00],
    [9, 7, 3, 2.00, 6.00]
]

ultimo_id_venda = 9

#Funções usadas no setor VENDAS

def listar_vendas():
    print("=" * 49)
    print("============     LISTA DE VENDAS     ============")
    print("=" * 49)

    #Agrupa os itens por ID de venda
    vendas_agrupadas = {}
    for venda in vendas:
        id_venda = venda[0]
        if id_venda not in vendas_agrupadas:
            vendas_agrupadas[id_venda] = []
        vendas_agrupadas[id_venda].append(venda)

    for id_venda, itens in vendas_agrupadas.items():
        total_venda = sum(item[4] for item in itens)
        print(f"\nVenda #{id_venda}  |  Total: R${total_venda:.2f}")
        print("-" * 65)
        for item in itens:
            produto = buscar_produto(item[1])
            nome_produto = produto[1] if produto else "Produto não encontrado"
            print(f"  Produto: {nome_produto} | Qtd: {item[2]} | Unit.: R${item[3]:.2f} | Subtotal: R${item[4]:.2f}")

#Função para registrar uma nova venda
def registrar_venda():
    global ultimo_id_venda
    
    print("=" * 49)
    print("============     REGISTRAR VENDA     ============")
    print("=" * 49)
    
    total = 0
    itens_adicionados = []
    
    ver_lista_produtos()
    while True:
        id_produto = int(input("Digite o ID do produto a ser vendido (0 para finalizar): "))    
        
        if id_produto == 0:
            break
        
        produto = buscar_produto(id_produto)
        if produto is None:
            print("ERRO: Produto não encontrado. Tente novamente.")
            continue
        
        quantidade = int(input("Digite a quantidade a ser vendida: "))
        if quantidade > produto[3]:
            print("ERRO: Quantidade insuficiente em estoque. Tente novamente.")
            print(f"Quantidade disponível: {produto[3]}")
            continue
        
        subtotal = quantidade * produto[2]
        total += subtotal
        
        produto[3] -= quantidade
        
        itens_adicionados.append([id_produto, quantidade, produto[2], subtotal])
        
        print("-" * 50)
        print(f"Produto adicionado à venda.")
        print("-" * 50)

    if not itens_adicionados:
        print("Nenhum produto adicionado. Venda cancelada.")
        return

    ultimo_id_venda += 1
    for item in itens_adicionados:
        vendas.append([ultimo_id_venda, item[0], item[1], item[2], item[3]])

    print("-" * 50)
    print(f"Venda finalizada. Total a pagar: R${total:.2f}")

#Função para excluir uma venda registrada
def excluir_venda():
    print("=" * 49)
    print("=============     EXCLUIR VENDA     =============")
    print("=" * 49)
    
    id_venda = int(input("Digite o ID da venda: "))
    
    encontrou = False
    for venda in vendas[:]:
        if venda[0] == id_venda:
            produto = buscar_produto(venda[1])
            if produto:
                produto[3] += venda[2]
            vendas.remove(venda)
            encontrou = True
    
    print("-" * 50)
    if encontrou:
        print("Venda removida com sucesso!")
    else:
        print("ERRO: Venda não encontrada.")
    print("-" * 50)

#Função para excluir todas as vendas registradas
def excluir_todas_as_vendas():
    global ultimo_id_venda

    print("=" * 49)
    print("========     EXCLUIR TODAS AS VENDAS     ========")
    print("=" * 49)

    confirmacao = input("Tem certeza que deseja excluir TODAS as vendas? (1 - Sim, 0 - Não): ")
    
    if confirmacao != "1":
        print("Operação cancelada.")
        return

    vendas.clear()
    ultimo_id_venda = 0

    print("-" * 50)
    print("Todas as vendas foram excluídas!")
    print("-" * 50)

#Função para exibir o menu de opções do setor VENDAS
def menu_vendas():
    while True:
        print("=" * 49)
        print("==============     MENU VENDAS     ==============")
        print("=" * 49)

        print("1 - Listar Vendas")
        print("2 - Registrar Venda")
        print("3 - Excluir Venda")
        print("4 - Excluir Todas as Vendas")
        print("0 - Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                listar_vendas()
            case "2":
                registrar_venda()
            case "3":
                excluir_venda()
            case "4":
                excluir_todas_as_vendas()
            case "0":
                print("Voltando ao menu principal.")
                break
            case _:
                print("Opção inválida. Tente novamente.")