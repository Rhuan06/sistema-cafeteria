from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from controllers.produto_controller import ProdutoController
from controllers.pedido_controller import PedidoController
from models.produto import Produto
from models.pedido import Pedido, ItemPedido

# Instancia a API e o Controlador
app = FastAPI(title="API Cafeteria - Produto")

# --- BLOCO DO CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Em produção colocaríamos o endereço exato do site. "*" libera para qualquer um.
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, DELETE, etc.
    allow_headers=["*"],
)
produto_controller = ProdutoController()
pedido_controller = PedidoController()


# Criando um 'Schema' (Molde) para validar os dados que vão chegar do Front-end
class ProdutoRequest(BaseModel):
    nome: str
    preco: float

# ROTA 1: Listar produtos (GET)
@app.get("/produtos", tags=["Produtos"])
def listar_produtos():
    produtos_objetos = produto_controller.listar_produtos()
    # Converte os objetos Python para dicionários para virarem JSON
    produtos_json = [{"id": p.id, "nome": p.nome, "preco": p.preco} for p in produtos_objetos]
    return produtos_json

# Rota 2: Criar Produto (POST)
@app.post("/produtos", tags=["Produtos"])
def criar_produto(produto: ProdutoRequest):
    # 1. Puxa todos os produtos que já estão no banco
    produtos_existentes = produto_controller.listar_produtos()

    # 2. Verifica se o nome digitado já existe na lista (transformando tudo em minúsculo para garantir)
    for p in produtos_existentes:
        if p.nome.lower() == produto.nome.lower():
            raise HTTPException(status_code=400, detail=f"O produto '{produto.nome}' já está cadastrado no cardápio.")

    novo_produto = Produto(nome=produto.nome, preco=produto.preco)
    sucesso = produto_controller.cadastrar_produto(novo_produto)

    if sucesso:
        return {"mensagem": f"Produto '{produto.nome}' cadastrado com sucesso!", "id": novo_produto.id}
    else:
        raise HTTPException(status_code=400, detail="Erro ao salvar no banco de dados.")
    
# ROTA 3: Deletar Produto (DELETE)
@app.delete("/produtos/{id_produto}", tags=["Produtos"])
def deletar_produto(id_produto: int):
    sucesso = produto_controller.deletar_produto(id_produto)
    if sucesso:
        return {"mensagem": f"Produto ID {id_produto} deletado com sucesso."}
    else:
        raise HTTPException(status_code=404, detail="Produto não encontrado ou não pôde ser deletado.")
    
# ROTAS DE PEDIDOS (VENDAS)

# Schemas para validar
class ItemPedidoRequest(BaseModel):
    produto_id: int
    quantidade: int = Field(gt=0)

class PedidoRequest(BaseModel):
    itens: List[ItemPedidoRequest]

# ROTA 4: Listar Pedidos (GET)
@app.get("/pedidos", tags=["Pedidos"])
def listar_pedidos():
    return pedido_controller.listar_pedidos()

# ROTA 5: Criar Pedido (POST)
@app.post("/pedidos", tags=["Pedidos"])
def criar_pedido(pedido_request: PedidoRequest):
    novo_pedido = Pedido()
    produtos_disponiveis = produto_controller.listar_produtos()

    # Monta o pedido em memória validando cada item
    for item in pedido_request.itens:
        produto_escolhido = next((p for p in produtos_disponiveis if p.id == item.produto_id), None)

        if not produto_escolhido:
            raise HTTPException(status_code=404, detail=f"Produto ID {item.produto_id} não existe no estoque.")
        
        novo_item = ItemPedido(produto=produto_escolhido, quantidade=item.quantidade)
        novo_pedido.adicionar_item(novo_item)

    # Dispara a transação com o banco de dados
    if novo_pedido.obter_itens():
        sucesso = pedido_controller.salvar_pedido(novo_pedido)
        if sucesso:
            return {"mensagem": "Pedido registrado com sucesso!", "total": novo_pedido.valor_total}
        else:
            raise HTTPException(status_code=400, detail="Erro interno ao salvar o pedido no banco.")
    else:
        raise HTTPException(status_code=400, detail="O pedido não pode estar vazio.")
    
# Rota 6: Cancelar Pedido (DELETE)
@app.delete("/pedidos/{id_pedido}", tags=["Pedidos"])
def cancelar_pedido(id_pedido: int):
    sucesso = pedido_controller.cancelar_pedido(id_pedido)
    if sucesso:
        return {"mensagem": f"Pedido {id_pedido} cancelado com sucesso."}
    else:
        raise HTTPException(status_code=404, detail="Aviso: Nenhum pedido encontrado com este ID.")

