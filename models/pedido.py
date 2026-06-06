from typing import List
from datetime import datetime
from .produto import Produto

class ItemPedido:
    def __init__(self, produto: Produto, quantidade: int = 1):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser um número maior que zero.")
        self.produto = produto
        self.quantidade = quantidade

    @property
    def subtotal(self) -> float:
        return self.produto.preco * self.quantidade
    
class Pedido:
    def __init__(self, id_pedido: int | None = None, data_hora: datetime | None = None):
        self.id = id_pedido
        # Se nenhuma data for passada, pega o momento exato da criação
        self.data_hora = data_hora or datetime.now()
        # lista protegida para guardar os itens comprados
        self._itens: List[ItemPedido] = []

    def adicionar_item(self, item: ItemPedido):
        self._itens.append(item)

    @property
    def valor_total(self) -> float:
        return sum(item.subtotal for item in self._itens)
    
    def obter_itens(self) -> List[ItemPedido]:
        return self._itens
    
    def __str__(self):
        return f"Pedido(ID: {self.id}, Data: {self.data_hora.strftime('%d/%m/%Y %H:%M')}, Itens: {len(self._itens)}, Total: R${self.valor_total:.2f})"
