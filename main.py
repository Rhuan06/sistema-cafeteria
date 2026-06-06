from controllers.produto_controller import ProdutoController
from controllers.pedido_controller import PedidoController
from models.produto import Produto
from models.pedido import Pedido, ItemPedido

def exibir_menu():
    """Exibe as opções do sistema no terminal."""
    print("\n" + "="*35)
    print("☕ SISTEMA DE GESTÃO - CAFETERIA ☕")
    print("="*35)
    print("--- GERENCIAR PRODUTOS ---")
    print("1. Cadastrar Novo Produto")
    print("2. Listar Produtos")
    print("3. Atualizar Preço de Produto")
    print("4. Deletar Produto")
    print("\n--- GERENCIAR VENDAS ---")
    print("5. Fazer Novo Pedido")
    print("6. Listar Histórico de Pedidos")
    print("7. Cancelar Pedido")
    print("\n0. Sair")
    print("="*35)

def main():
    # Instanciando os controladores que vão conversar com o banco
    produto_controller = ProdutoController()
    pedido_controller = PedidoController()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        match opcao:
            case '1':
                print("\n--- Novo Produto ---")
                nome = input("Digite o nome do produto: ")
                try:
                    preco = float(input("Digite o preço (ex: 5.50): "))
                    novo_produto = Produto(nome=nome, preco=preco)
                    produto_controller.cadastrar_produto(novo_produto)
                except ValueError as e:
                    print(f"Erro de validação: {e}")

            case '2':
                print("\n--- Estoque Atual ---")
                produtos = produto_controller.listar_produtos()
                if not produtos:
                    print("Nenhum produto cadastrado ainda.")
                else:
                    for p in produtos:
                        print(p)

            case '3':
                print("\n--- Atualizar Preço ---")
                try:
                    id_prod = int(input("Digite o ID do produto: "))
                    novo_preco = float(input("Digite o novo preço: "))
                    produto_controller.atualizar_preco(id_produto=id_prod, novo_preco=novo_preco)
                except ValueError:
                    print("Erro: ID e Preço devem ser numéricos.")

            case '4':
                print("\n--- Deletar Produto ---")
                try:
                    id_prod = int(input("Digite o ID do produto a ser excluído: "))
                    produto_controller.deletar_produto(id_produto=id_prod)
                except ValueError:
                    print("Erro: O ID deve ser um número inteiro.")
                    
            case '5':
                print("\n--- Novo Pedido ---")
                produtos_disponiveis = produto_controller.listar_produtos()
                
                if not produtos_disponiveis:
                    print("Erro: Cadastre pelo menos um produto antes de fazer um pedido.")
                    continue
                    
                print("Cardápio:")
                for p in produtos_disponiveis:
                    print(f"[{p.id}] {p.nome} - R${p.preco:.2f}")
                    
                novo_pedido = Pedido()

                while True:
                    escolha_id = input("\nDigite o ID do produto (ou '0' para finalizar): ")
                    if escolha_id == '0':
                        break
                        
                    try:
                        id_prod = int(escolha_id)
                        produto_escolhido = next((p for p in produtos_disponiveis if p.id == id_prod), None)
                        
                        if produto_escolhido:
                            qtd = int(input(f"Quantidade de {produto_escolhido.nome}: "))
                            novo_item = ItemPedido(produto=produto_escolhido, quantidade=qtd)
                            novo_pedido.adicionar_item(novo_item)
                            print(f"Adicionado: {qtd}x {produto_escolhido.nome}")
                        else:
                            print("ID de produto não encontrado.")
                    except ValueError as e:
                        print(f"Erro: {e}")
                
                if novo_pedido.obter_itens():
                    pedido_controller.salvar_pedido(novo_pedido)
                else:
                    print("Pedido cancelado (carrinho vazio).")

            case '6':
                print("\n--- Histórico de Pedidos ---")
                pedidos = pedido_controller.listar_pedidos()
                if not pedidos:
                    print("Nenhum pedido registrado ainda.")
                else:
                    for ped in pedidos:
                        print(f"Pedido [{ped['id']}] - Data: {ped['data']} - Total: R${ped['total']:.2f}")

            case '7':
                print("\n--- Cancelar Pedido ---")
                try:
                    id_ped = int(input("Digite o ID do pedido a ser cancelado: "))
                    pedido_controller.cancelar_pedido(id_pedido=id_ped)
                except ValueError:
                    print("Erro: O ID deve ser um número inteiro.")
                    
            case '0':
                print("\nEncerrando o sistema da cafeteria... Até logo!")
                break
                
            case _:
                print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()