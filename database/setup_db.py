from database.conexao import obter_conexao

class ConfiguradorBanco:
    def __init__(self):
        self.conexao = obter_conexao()

    def criar_tabelas(self):
        if not self.conexao:
            print("Erro: Não foi possível obter conexão com o banco para criar as tabelas.")
            return
        
        # Cria as tabelas necessárias para o sistema
        sql_tabelas = """
        DROP TABLE IF EXISTS itens_pedido CASCADE;
        DROP TABLE IF EXISTS pedidos CASCADE;
        DROP TABLE IF EXISTS produtos CASCADE;

        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco NUMERIC(10, 2) NOT NULL
        );

        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            valor_total NUMERIC(10, 2) DEFAULT 0.0
        );

        CREATE TABLE IF NOT EXISTS itens_pedido (
            pedido_id INTEGER REFERENCES pedidos(id) ON DELETE CASCADE,
            produto_id INTEGER REFERENCES produtos(id) ON DELETE RESTRICT,
            quantidade INTEGER DEFAULT 1,
            PRIMARY KEY (pedido_id, produto_id)
        );
        """

        try:
            cursor = self.conexao.cursor()
            cursor.execute(sql_tabelas)
            self.conexao.commit()
            print("Tabelas criadas com sucesso.")
        except Exception as e:
            print(f"Erro ao criar as tabelas: {e}")
        finally:
            if 'cursor'in locals():
                cursor.close()

    def fechar_conexao(self):
        if self.conexao:
            self.conexao.close()
            print("Conexao com o banco de dados fechada.")

if __name__ == "__main__":
    setup = ConfiguradorBanco()
    setup.criar_tabelas()
    setup.fechar_conexao()