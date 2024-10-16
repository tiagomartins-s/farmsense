import oracledb
from src.database.connection import create_connection, close_connection
from src.utils.log import record_log

def insert_humidity(humidity, alert, date):
    conn = create_connection()
    if conn is None:
        record_log("Sistema indicou falha na conexão.")
        print("Falha na conexão.")
        return

    try:
        cursor = conn.cursor()
        sql = """
        INSERT INTO UMIDADE (UMIDADE, ALERTA, DATA)
        VALUES (:1, :2, :3)
        """
        cursor.execute(sql, (humidity, alert, date))
        conn.commit()
        record_log("Registro de umidade inserido com sucesso.")
        print("Registro de umidade inserido com sucesso.")
    except oracledb.DatabaseError as e:
        record_log(f"Erro ao inserir umidade: {e}")
        print(f"Erro ao inserir umidade: {e}")
    finally:
        close_connection(conn)


def last_humidity():
    conn = create_connection()
    if conn is None:
        record_log("Sistema indicou falha na conexão.")
        print("Falha na conexão.")
        return

    try:
        cursor = conn.cursor()

        sql = """
        SELECT UMIDADE, ALERTA, DATA FROM (
            SELECT UMIDADE, ALERTA, DATA, 
                   ROW_NUMBER() OVER (ORDER BY DATA DESC) AS RN
            FROM UMIDADE
        ) WHERE RN = 1
        """

        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            humidity, alert, date = result
            formated_date = date.strftime('%Y-%m-%d')
            return {
                "umidade": humidity,
                "alerta": alert,
                "data": formated_date
            }
        else:
            record_log("Sistema indicou nenhuma umidade cadastrada.")
            print("Nenhuma umidade registrada.")
            return None

    except oracledb.DatabaseError as e:
        error, = e.args
        record_log(f"Erro ao buscar a última umidade: Código {error.code}, Mensagem: {error.message}")
        print(f"Erro ao buscar a última umidade: Código {error.code}, Mensagem: {error.message}")
    finally:
        close_connection(conn)