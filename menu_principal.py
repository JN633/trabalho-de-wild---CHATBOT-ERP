from estoque import menu_estoque
from vendas import menu_vendas

while True:
    print("=" * 50)
    print("=============     MENU PRINCIPAL     =============")
    print("=" * 50)

    print("1 - Gerenciar Estoque")
    print("2 - Gerenciar Vendas")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_estoque()
    
    elif opcao == "2":
        menu_vendas()
    
    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break
    
    else:
        print("Opção inválida. Tente novamente.")