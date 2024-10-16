import json
import os
import oracledb
from datetime import datetime
from collections import defaultdict
from src.database.connection import create_connection, close_connection
from src.utils.log import record_log

def get_last_temperatura_umidade_per_day():
    conn = create_connection()
    if conn is None:
        record_log("Sistema indicou falha na conexão.")
        print("Falha na conexão.")
        return

    try:
        cursor = conn.cursor()

        sql = """
        SELECT
            t.DATA,
            t.TEMPERATURA,
            u.UMIDADE
        FROM (
            SELECT TEMPERATURA, ALERTA, DATA,
                   ROW_NUMBER() OVER (PARTITION BY DATA ORDER BY DATA DESC) AS rn
            FROM TEMPERATURA
        ) t
        JOIN (
            SELECT UMIDADE, ALERTA, DATA,
                   ROW_NUMBER() OVER (PARTITION BY DATA ORDER BY DATA DESC) AS rn
            FROM UMIDADE
        ) u
        ON t.DATA = u.DATA AND t.rn = u.rn
        ORDER BY t.DATA DESC
        """

        cursor.execute(sql)
        results = cursor.fetchall()

        items = []
        for row in results:
            date, temperature, humidity = row
            formated_date = date.strftime('%Y-%m-%d')
            items.append({
                "data": formated_date,
                "temperatura": temperature,
                "umidade": humidity,
            })

        if items:
            return items
        else:
            record_log("Sistema indicou falta de registros para geração de log.")
            print("Nenhum registro de temperatura e umidade encontrado.")
            return None

    except oracledb.DatabaseError as e:
        error, = e.args
        record_log(f"Sistema indicou erro ao buscar temperatura e umidade por dia: Código {error.code}, Mensagem: {error.message}")
        print(f"Erro ao buscar temperatura e umidade por dia: Código {error.code}, Mensagem: {error.message}")
    finally:
        close_connection(conn)

def irrigation_need(temperatura, umidade):
    if temperatura > 30 and umidade < 40:
        return "Recomendar irrigação"
    elif umidade > 70 and temperatura < 30:
        return "Suspender irrigação"
    else:
        return "Nenhuma ação"

def generate_report():
    items = get_last_temperatura_umidade_per_day()

    if not items:
        record_log("Sistema interrompeu geração de relatório por falta de dados.")
        print("Nenhum dado encontrado para gerar o relatório.")
        return

    irrigation_by_month = defaultdict(lambda: {"necessidade": 0, "total_dias": 0})

    for item in items:
        date = datetime.strptime(item["data"], "%Y-%m-%d")
        month = date.month

        temperature = item["temperatura"]
        humidity = item["umidade"]

        action = irrigation_need(temperature, humidity)

        irrigation_by_month[month]["total_dias"] += 1
        if action == "Recomendar irrigação":
            irrigation_by_month[month]["necessidade"] += 1

    total_days_year = sum(month_date["total_dias"] for month_date in irrigation_by_month.values())
    percentage_by_month = []

    for month, data in irrigation_by_month.items():
        need = data["necessidade"]
        total_days = data["total_dias"]

        if total_days > 0:
            percentage = (need / total_days_year) * 100
        else:
            percentage = 0

        percentage_by_month.append({
            "mes": month,
            "porcentagem_irrigacao": round(percentage, 2)
        })

    percentage_by_month.sort(key=lambda x: x["porcentagem_irrigacao"])

    report_directory = "data/reports"

    current_date = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = f"report-{current_date}.json"
    file_path = report_directory + "/" + file_name
    relatorio = {
        "meses": percentage_by_month
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(relatorio, f, ensure_ascii=False, indent=4)

    record_log(f"Relatório gerado com sucesso: {file_path}")
    print(f"Relatório gerado com sucesso: {file_path}")
