from estoque import menu_estoque
from vendas import menu_vendas
from relatorios import menu_relatorios

while True:
    print("=" * 50)
    print("=============     MENU PRINCIPAL     =============")
    print("=" * 50)

    print("1 - Gerenciar Estoque")
    print("2 - Gerenciar Vendas")
    print("3 - Emitir Relatórios")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            menu_estoque()
        case "2":
            menu_vendas()
        case "3":
            menu_relatorios()
        case "0":
            print("Saindo do programa...")
            break
        case _:
            print("Opção inválida. Tente novamente.")