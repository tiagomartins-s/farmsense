import os
from datetime import datetime

def view_log():
    try:
        with open('data/log.txt', 'r', encoding='utf-8') as log_file:
            print(log_file.read())
    except FileNotFoundError:
        record_log("Sistema indicou arquivo log não encontrado.")
        print("Arquivo de log não encontrado.")
    except Exception as e:
        record_log(f"Ocorreu um erro ao ler o log: {e}")
        print(f"Ocorreu um erro ao ler o log: {e}")

def record_log(message):
    log_directory = "data"
    os.makedirs(log_directory, exist_ok=True)
    current_date = datetime.now()
    formatted_datetime = current_date.strftime('%Y-%m-%d %H:%M:%S')
    file_path = os.path.join(log_directory, "log.txt")

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(f"{formatted_datetime}: {message}\n\n")