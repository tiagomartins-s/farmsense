import oracledb
from src.database.connection import create_connection, close_connection
from src.utils.log import record_log

def insert_temperature(temperature, alert, date):
    conn = create_connection()
    if conn is None:
        record_log("Sistema indicou falha na conexão.")
        print("Falha na conexão.")
        return

    try:
        cursor = conn.cursor()
        sql = """
        INSERT INTO TEMPERATURA (TEMPERATURA, ALERTA, DATA)
        VALUES (:1, :2, :3)
        """
        cursor.execute(sql, (temperature, alert, date))
        conn.commit()
        record_log("Registro de temperatura inserido com sucesso.")
        print("Registro de temperatura inserido com sucesso.")
    except oracledb.DatabaseError as e:
        record_log(f"Erro ao inserir temperatura: {e}")
        print(f"Erro ao inserir temperatura: {e}")
    finally:
        close_connection(conn)

def last_temperature():
    conn = create_connection()
    if conn is None:
        record_log("Sistema indicou falha na conexão.")
        print("Falha na conexão.")
        return

    try:
        cursor = conn.cursor()

        sql = """
        SELECT TEMPERATURA, ALERTA, DATA FROM (
            SELECT TEMPERATURA, ALERTA, DATA, 
                   ROW_NUMBER() OVER (ORDER BY DATA DESC) AS RN
            FROM TEMPERATURA
        ) WHERE RN = 1
        """

        cursor.execute(sql)
        result = cursor.fetchone()

        if result:
            temperature, alert, date = result
            formated_date = date.strftime('%Y-%m-%d')
            return {
                "temperatura": temperature,
                "alerta": alert,
                "data": formated_date
            }
        else:
            record_log("Sistema indicou nenhuma temperatura cadastrada.")
            print("Nenhuma temperatura registrada.")
            return None

    except oracledb.DatabaseError as e:
        error, = e.args
        record_log(f"Erro ao buscar a última temperatura: Código {error.code}, Mensagem: {error.message}")
        print(f"Erro ao buscar a última temperatura: Código {error.code}, Mensagem: {error.message}")
    finally:
        close_connection(conn)