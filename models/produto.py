# Criando a classe Produto

class Produto:
    def __init__(self, nome: str, preco: float, id_produto: int | None = None):
        self.id = id_produto
        self.nome = nome
        self.preco = preco

    @property
    def preco(self) -> float:
        return self._preco
    
    @preco.setter
    def preco(self, valor: float):
        #Valida e define o preço d produto
        if valor < 0:
            raise ValueError("Erro de validação: O preço do produto não pode ser negativo.")
        self._preco = float(valor)

    def __str__(self):
        # formata a exibição do produto
        return f"Produto(ID: {self.id}, Nome: '{self.nome}', Preço: R${self.preco:.2f})"
