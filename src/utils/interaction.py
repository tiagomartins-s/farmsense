from src.utils.log import record_log

def receives_float(label):
    while True:
        try:
            value = float(input(f"{label}: "))
            value = round(value, 2)
            return value
        except ValueError:
            record_log("Sistema captou erro de número inválido vindo do usuário.")
            print("Erro: Por favor, insira um número válido com duas casas decimais.")