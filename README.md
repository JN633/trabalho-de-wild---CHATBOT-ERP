# Segunda Versão
Sistema de automação comercial desenvolvido em Python, com gerenciamento de estoque e vendas, persistência de dados em arquivos e emissão de relatórios.

# Equipe
Gustavo Santana
Jone Mauricío
Enzzo Mauricío
Artur Ribeiro

# Descrição dos Setores
# Setor 1 — Estoque
Responsável pelo cadastro e controle dos produtos disponíveis na loja.
Permite listar, cadastrar, atualizar e excluir produtos, além de controlar as quantidades em estoque.

# Setor 2 — Vendas
Responsável pelo registro e controle das vendas realizadas.
Permite registrar novas vendas (com desconto automático do estoque), listar, excluir e calcular o total arrecadado.

# Funcionalidades
- [x] Gerenciamento completo de estoque (listar, cadastrar, atualizar, excluir)
- [x] Registro e controle de vendas
- [x] Persistência de dados em arquivos `.txt`
- [x] Carga automática dos dados ao iniciar o programa
- [x] Salvamento automático após cada operação
- [x] Emissão de relatório geral de vendas (com nome dos produtos)
- [x] Emissão de relatório filtrado por produto

# Arquivos de Dados

Os dados são salvos automaticamente em:

| Arquivo | Conteúdo |
|---|---|
| `dados/estoque.txt` | Produtos cadastrados (ID, nome, preço, quantidade) |
| `dados/vendas.txt` | Vendas registradas (ID venda, ID produto, qtd, preço, subtotal) |