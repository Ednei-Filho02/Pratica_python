produtos = [
    {
        'nome':"arroz",
        'valor': 5.5,
        'quantidade': 12 
    },
    {
        'nome':"feijão",
        'valor': 10.5,
        'quantidade': 5
    }
]


def adicionar_produto():
    while True:
        nome_produto = str(input("Digite o nome do produto: "))
        valor_produto = float(input(f"Digite o valor de {nome_produto}: ").replace(',', '.'))
        quantidade_produto = int(input(f"Digite a quantidade de {nome_produto} no estoque: "))
        produtos.append({
                'nome': nome_produto,
                'valor': valor_produto,
                'quantidade': quantidade_produto
            })

        # Verifica se deseja cadastrar outro produto
        controle = input('Deseja adicionar outro produto? (s/n): ')

        if controle.lower() != 's':
            break

def listar_produtos(produtos):
    for i, produto in enumerate(produtos, start=1):
        print(
            f"{i}. {produto['nome']} | "
            f"Valor: R$ {produto['valor']:.2f} | "
            f"Quantidade: {produto['quantidade']}"
        )

def estoque_produto():
    for i, produto in enumerate(produtos, start=1):
            print(f"{i}. {produto['nome']}")
    nome = input("Digite o nome do produto: ").lower()

    for produto in produtos:
        if produto['nome'].lower() == nome:
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade em estoque: {produto['quantidade']}")
            print(f"Valor unitário: R$ {produto['valor']:.2f}")
            print(f"Valor total: R$ {produto['valor'] * produto['quantidade']:.2f}")
            return

    print("Produto não encontrado!")


def estoque_geral():
    quantidade_total = 0
    valor_total = 0

    for produto in produtos:
        quantidade_total += produto['quantidade']
        valor_total += produto['valor'] * produto['quantidade']

    print("\n=== ESTOQUE GERAL ===")
    print(f"Quantidade total de itens: {quantidade_total}")
    print(f"Valor total do estoque: R$ {valor_total:.2f}")

while True:
    print("\n==== MENU ====")
    print("1 - Adicionar produto")
    print("2 - Listar produtos")
    print("3 - Consultar estoque de um produto")
    print("4 - Consultar estoque geral")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            adicionar_produto()

        case "2":
            print("\n=== Produtos cadastrados ===")
            listar_produtos(produtos)

        case "3":
            estoque_produto()

        case "4":
            estoque_geral()

        case "5":
            print("Encerrando o programa...")
            break

        case _:
            print("Opção inválida! Tente novamente.")