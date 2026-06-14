import os
from datetime import datetime
from estoque import buscar_produto
from vendas import vendas

#Variável para o nome da pasta onde os relatórios serão salvos, para facilitar a mudança futura, caso necessário
PASTA_RELATORIOS = "relatorios"


#Função para criar o cabeçalho dos relatórios
def cabecalho(f, titulo):
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    f.write("=" * 65 + "\n")
    f.write("== SUPERMERCADO CORAÇÃO - SISTEMA ERP\n")
    f.write(f"== {titulo}\n")
    f.write(f"== Gerado em: {agora}\n")
    f.write("=" * 65 + "\n\n")


#Função para criar o rodapé dos relatórios
def rodape(f, total_registros, valor_total=None):
    f.write("\n" + "=" * 65 + "\n")
    f.write(f"  Total de registros: {total_registros}\n")
    if valor_total is not None:
        f.write(f"  Valor Total: R$ {valor_total:.2f}\n")
    f.write("=" * 65 + "\n")


#Função para gerar relatório geral de vendas
def relatorio_geral():
    os.makedirs(PASTA_RELATORIOS, exist_ok=True)
    caminho = os.path.join(PASTA_RELATORIOS, "relatorio_geral.txt")

    vendas_agrupadas = {}
    for v in vendas:
        id_venda = v[0]
        if id_venda not in vendas_agrupadas:
            vendas_agrupadas[id_venda] = []
        vendas_agrupadas[id_venda].append(v)

    total_registros = len(vendas_agrupadas)
    valor_total = sum(v[4] for v in vendas)

    with open(caminho, "w", encoding="utf-8") as f:
        cabecalho(f, "RELATÓRIO GERAL DE VENDAS")

        col = f"  {'Venda':<8} {'Produto':<20} {'Qtd':>5} {'Unit.':>10} {'Subtotal':>12}\n"
        f.write(col)
        f.write("-" * 65 + "\n")

        for id_venda, itens in vendas_agrupadas.items():
            total_venda = sum(item[4] for item in itens)
            f.write(f"\n  VENDA #{id_venda}  —  Total: R$ {total_venda:.2f}\n")
            for item in itens:
                produto = buscar_produto(item[1])
                nome = produto[1] if produto else "Produto não encontrado"
                f.write(
                    f"  {'':8} {nome:<20} {item[2]:>8} "
                    f"    R${item[3]:.2f}     R${item[4]:.2f}\n"
                )

        rodape(f, total_registros, valor_total)

    print(f"Relatório gerado com sucesso: {caminho}")


#Função para gerar relatório de vendas filtrado por produto
def relatorio_por_produto():
    from estoque import listar_produtos

    listar_produtos()
    id_produto = int(input("Digite o ID do produto para filtrar: "))
    produto = buscar_produto(id_produto)

    if produto is None:
        print("ERRO: Produto não encontrado.")
        return

    os.makedirs(PASTA_RELATORIOS, exist_ok=True)
    caminho = os.path.join(PASTA_RELATORIOS, f"relatorio_produto_{id_produto}.txt")

    itens_filtrados = [v for v in vendas if v[1] == id_produto]

    total_registros = len(itens_filtrados)
    valor_total = sum(v[4] for v in itens_filtrados)
    qtd_total = sum(v[2] for v in itens_filtrados)

    with open(caminho, "w", encoding="utf-8") as f:
        cabecalho(f, f"RELATÓRIO DE VENDAS — PRODUTO: {produto[1].upper()}")

        f.write(f"  Produto  : {produto[1]}\n")
        f.write(f"  Preço    : R$ {produto[2]:.2f}\n")
        f.write(f"  Em estoque: {produto[3]} unidades\n\n")

        col = f"  {'Venda':<8} {'Qtd':>5} {'Preço Unit.':>12} {'Subtotal':>12}\n"
        f.write(col)
        f.write("-" * 65 + "\n")

        for item in itens_filtrados:
            f.write(
                f"  #{item[0]:<7} {item[2]:>5} "
                f"R${item[3]:>10.2f} R${item[4]:>10.2f}\n"
            )

        f.write("\n")
        f.write(f"  Qtd. total vendida: {qtd_total} unidades\n")
        rodape(f, total_registros, valor_total)

    print(f"Relatório gerado com sucesso: {caminho}")

#Menu para acessar os relatórios
def menu_relatorios():
    while True:
        print("=" * 49)
        print("===========     EMITIR RELATÓRIOS     ===========")
        print("=" * 49)

        print("1 - Relatório Geral de Vendas")
        print("2 - Relatório por Produto")
        print("0 - Voltar ao Menu Principal")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            relatorio_geral()
        elif opcao == "2":
            relatorio_por_produto()
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
