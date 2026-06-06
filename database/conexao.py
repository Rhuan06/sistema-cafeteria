import os
import psycopg2
from dotenv import load_dotenv

# carrega as variaveis do arquivo .env
load_dotenv()

def obter_conexao():
    # Estabelece e retorna uma conexão com o banco de dados
    try:
        conexao = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            dbname=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD')
        )
        return conexao
    except psycopg2.OperationalError as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
