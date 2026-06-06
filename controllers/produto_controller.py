from database.conexao import obter_conexao
from database.queries import INSERIR_PRODUTO, BUSCAR_TODOS_PRODUTOS, ATUALIZAR_PRODUTO, DELETAR_PRODUTO
from models.produto import Produto

class ProdutoController:
    def cadastrar_produto(self, produto: Produto) -> bool:
        # Cadastrar um novo produto no banco de dados
        conexao = obter_conexao()
        if not conexao:
            return False
        
        try:
            cursor = conexao.cursor()
            cursor.execute(INSERIR_PRODUTO, (produto.nome, produto.preco))

            produto.id = cursor.fetchone()[0]
            conexao.commit()
            print(f"Sucesso: {produto.nome} cadastrado com o ID {produto.id}!")
            return True
        except Exception as e:
            print(f"Erro ao cadastrar produto: {e}")
            return False
        finally:
            cursor.close()
            conexao.close()

    def listar_produtos(self) -> list[Produto]:
        # Lista todos os produtos cadastrados no BD
        conexao = obter_conexao()
        produtos = []

        if not conexao:
            return produtos
        
        try:
            cursor = conexao.cursor()
            cursor.execute(BUSCAR_TODOS_PRODUTOS)
            linhas = cursor.fetchall()

            for linha in linhas:
                produto = Produto(id_produto=linha[0], nome=linha[1], preco=linha[2])
                produtos.append(produto)

            return produtos
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")
            return produtos
        finally:
            cursor.close()
            conexao.close()

    def atualizar_preco(self, id_produto: int, novo_preco: float) -> bool:
        # Atualiza os preços existentes no BD
        if novo_preco < 0:
            print("Erro: O preço não pode ser negativo.")
            return False
        
        conexao = obter_conexao()
        if not conexao:
            return False
        
        try:
            cursor = conexao.cursor()
            cursor.execute(ATUALIZAR_PRODUTO, (novo_preco, id_produto))

            # Verificar se a atualização foi bem-sucedida
            if cursor.rowcount == 0:
                print(f"Aviso: Nenhum produto encontrado com o ID {id_produto}.")
                return False
            
            conexao.commit()
            print(f"Sucesso: Preço do produto ID {id_produto} atualizado para R${novo_preco:.2f}!")
            return True
        except Exception as e:
            print(f"Erro ao atualizar produto: {e}")
            conexao.rollback()
            return False
        finally:
            cursor.close()
            conexao.close()

    def deletar_produto(self, id_produto: int) -> bool:
        # Deleta produto do BD
        conexao = obter_conexao()
        if not conexao:
            return False
        
        try:
            cursor = conexao.cursor()
            cursor.execute(DELETAR_PRODUTO, (id_produto,))

            if cursor.rowcount == 0:
                print(f"Aviso: Nenhum produto encontrado com o ID {id_produto}.")
                return False
            
            conexao.commit()
            print(f"Sucesso: Produto ID {id_produto} foi excluído do sistema.")
            return True
        except Exception as e:
            # Captura erros de restrição, como tentar apagar um produto que já está em um pedido
            print(f"Erro ao deletar produto: {e}")
            conexao.rollback()
            return False
        finally:
            cursor.close()
            conexao.close()

