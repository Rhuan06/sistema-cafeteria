# QUERIES DA TABELA: PRODUTOS

INSERIR_PRODUTO = """
    INSERT INTO produtos (nome, preco)
    VALUES (%s, %s)
    RETURNING id;
"""

# 1. ATUALIZADO: Agora só busca os produtos que estão com ativo = TRUE
BUSCAR_TODOS_PRODUTOS = """
    SELECT id, nome, preco
    FROM produtos
    WHERE ativo = TRUE
    ORDER BY nome;
"""

ATUALIZAR_PRODUTO = """
    UPDATE produtos 
    SET preco = %s 
    WHERE id = %s;
"""

# 2. ATUALIZADO: tira o DELETE destrutivo pelo UPDATE (Desligar)
DELETAR_PRODUTO = """
    UPDATE produtos 
    SET ativo = FALSE 
    WHERE id = %s;
"""

# QUERIES DA TABELA: PEDIDOS E ITENS

INSERIR_PEDIDO = """
    INSERT INTO pedidos (data_hora, valor_total) 
    VALUES (%s, %s) 
    RETURNING id;
"""

INSERIR_ITEM_PEDIDO = """
    INSERT INTO itens_pedido (pedido_id, produto_id, quantidade) 
    VALUES (%s, %s, %s);
"""

BUSCAR_TODOS_PEDIDOS = """
    SELECT id, data_hora, valor_total 
    FROM pedidos 
    ORDER BY data_hora DESC;
"""

CANCELAR_PEDIDO = """
    DELETE FROM pedidos 
    WHERE id = %s;
"""