from database.conexao import obter_conexao
from database.queries import INSERIR_PEDIDO, INSERIR_ITEM_PEDIDO, BUSCAR_TODOS_PEDIDOS, CANCELAR_PEDIDO
from models.pedido import Pedido

class PedidoController:
    def salvar_pedido(self, pedido: Pedido) -> bool:
        """
        Salva um pedido completo no banco de dados.
        Usa o conceito de Transação (ACID): ou salva tudo (pedido + itens), ou desfaz tudo.
        """
        # Verifica se o pedido tem itens
        if not pedido.obter_itens():
            print("Erro de Validação: Não é possível registrar um pedido vazio.")
            return False
        
        conexao = obter_conexao()
        if not conexao:
            return False
        
        try:
            cursor = conexao.cursor()

            # Passo 1: Inserir na tabela 'pedidos' e pegar o ID gerado
            cursor.execute(INSERIR_PEDIDO, (pedido.data_hora, pedido.valor_total))
            pedido.id = cursor.fetchone()[0]

            # Passo 2: Laço de repetição para inserir cada item na tabela 'itens_pedido'
            for item in pedido.obter_itens():
                cursor.execute(
                    INSERIR_ITEM_PEDIDO,
                    (pedido.id, item.produto.id, item.quantidade)
                )

            # Passo 3: Se tudo deu certo, confirma a transação
            conexao.commit()
            print(f"Sucesso: Pedido {pedido.id} registrado com {len(pedido.obter_itens())} itens! Total: R${pedido.valor_total:.2f}")
            return True       
        except Exception as e:
            # Se algo deu errado, desfaz a transação
            print(f"Falha crítica ao salvar o pedido. Transação revertida. Erro: {e}")
            conexao.rollback()
            return False        
        finally:
            cursor.close()
            conexao.close()

    def listar_pedidos(self) -> list[Pedido]:
        """
        Retorna uma lista de todos os pedidos registrados no banco de dados.
        """
        conexao = obter_conexao()
        pedidos_lista = []

        if not conexao:
            return pedidos_lista
        
        try:
            cursor = conexao.cursor()
            cursor.execute(BUSCAR_TODOS_PEDIDOS)
            linhas = cursor.fetchall()

            """Como a classe pedido é complexa, aqui podemos retornar dicionários ou tuplas simples apenas para exibição rápida no terminal"""
            for linha in linhas:
                pedidos_lista.append({
                    "id": linha[0],
                    "data": linha[1].strftime('%d/%m/%Y %H:%M'),
                    "total": linha[2]
                })

            return pedidos_lista
        except Exception as e:
            print(f"Erro ao buscar histórico de pedidos: {e}")
            return pedidos_lista
        finally:
            cursor.close()
            conexao.close()

    def cancelar_pedido(self, id_pedido: int) -> bool:
        """Ao excluir um pedido, os itens ligados a ele também serão excluídos automaticamente por conta do ON DELETE CASCADE definido na chave estrangeira."""
        conexao = obter_conexao()
        if not conexao:
            return False
        
        try:
            cursor = conexao.cursor()
            cursor.execute(CANCELAR_PEDIDO, (id_pedido,))
            
            if cursor.rowcount == 0:
                print(f"Aviso: Nenhum pedido encontrado com o ID {id_pedido}.")
                return False
                
            conexao.commit()
            print(f"Sucesso: O Pedido {id_pedido} foi cancelado e seus pedidos foram removidos do sistema.")
            return True
        except Exception as e:
            print(f"Erro ao tentar cancelar o pedido: {e}")
            conexao.rollback()
            return False
        finally:
            cursor.close()
            conexao.close()

