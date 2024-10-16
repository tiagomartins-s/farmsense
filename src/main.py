from utils.faker import generate_test_data
from utils.log import view_log, record_log
from database.report import generate_report
from utils.interaction import receives_float
from utils.check import status, check_temperature, check_humidity
from database.temperature import last_temperature, insert_temperature
from database.humidity import last_humidity, insert_humidity
from datetime import datetime
from database.clear import clear_base

def main_menu():
    print("Bem vindo a farmsense!")
    record_log("Sistema inicializado.")

    while True:
        print("")
        print("-------------------------------------------------------------------------------------------------------")
        print("")
        print("1. Cadastrar dados sensores")
        print("2. Verificar status plantação")
        print("3. Gerar relatório de meses")
        print("4. Ver logs de utilização da plataforma")
        print("5. Gerar dados teste (15 minutos 3 anos histórico)")
        print("6. Limpar base de dados")
        print("7. Sair")
        print("")
        print("-------------------------------------------------------------------------------------------------------")
        print("")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            record_log("Cadastro iniciado.")
            temperature = receives_float("Digite a informação do sensor de temperatura: ")
            humidity = receives_float("Digite a informação do sensor de umidade: ")
            temperature_alert = check_temperature(temperature)
            humidity_alert = check_humidity(humidity)
            date = datetime.now()
            insert_temperature(temperature, temperature_alert, date)
            insert_humidity(humidity, humidity_alert, date)
            record_log("Cadastro finalizado com sucesso.")
        elif choice == '2':
            record_log("Visualização de status iniciada.")
            temperature = last_temperature()
            humidity = last_humidity()
            if temperature is not None and humidity is not None:
                temperature_value = temperature.get('temperatura')
                humidity_value = humidity.get('umidade')
                status(temperature_value, humidity_value)
            else:
                print("Ainda não existem dados dos sensores. Cadastre dados e tente novamente!")
            record_log("Visualização de status finalizada com sucesso.")
        elif choice == '3':
            record_log("Geração de relatório iniciada.")
            generate_report()
            record_log("Geração de relatório finalizada com sucesso.")
        elif choice == '4':
            record_log("Visualização de log iniciada.")
            view_log()
            record_log("Visualização de log finalizada com sucesso.")
        elif choice == '5':
            record_log("Inserção de dados teste iniciada.")
            generate_test_data()
            record_log("Inserção de dados teste finalizada com sucesso.")
        elif choice == '6':
            record_log("Limpeza de base de dados iniciada.")
            clear_base()
            record_log("Limpeza de base de dados finalizada com sucesso.")
        elif choice == '7':
            record_log("Interação com sistema finalizada.")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main_menu()
