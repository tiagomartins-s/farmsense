import oracledb
from src.database.connection import create_connection, close_connection
from src.utils.log import record_log

def clear_base():
    conn = create_connection()
    if conn is None:
        record_log("Sistema indicou falha na conexão.")
        print("Falha na conexão.")
        return

    try:
        cursor = conn.cursor()

        cursor.execute("DELETE FROM TEMPERATURA")

        cursor.execute("DELETE FROM UMIDADE")

        conn.commit()
        print("A base de dados foi limpa com sucesso!")

    except oracledb.DatabaseError as e:
        conn.rollback()
        error, = e.args
        record_log(f"Erro ao deletar registros: Código {error.code}, Mensagem: {error.message}")
        print(f"Erro ao deletar registros: Código {error.code}, Mensagem: {error.message}")

    finally:
        close_connection(conn)