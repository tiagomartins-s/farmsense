import oracledb
from src.utils.log import record_log

def create_connection():
    try:
        connection = oracledb.connect(
            user="rm560639",                    # Usuário do banco de dados
            password="311299",                  # Senha do banco de dados
            dsn="oracle.fiap.com.br:1521/ORCL"  # Data Source Name (ex.: host:porta/serviço)
        )
        return connection

    except oracledb.DatabaseError as e:
        error, = e.args
        record_log(f"Erro ao conectar-se ao banco de dados: {error.message}")
        print(f"Erro ao conectar-se ao banco de dados: {error.message}")
        return None

def close_connection(connection):
    if connection:
        try:
            connection.close()
        except oracledb.DatabaseError as e:
            error, = e.args
            record_log(f"Erro ao encerrar a conexão: {error.message}")
            print(f"Erro ao encerrar a conexão: {error.message}")
