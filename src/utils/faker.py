import random
from datetime import datetime, timedelta
from src.database.temperature import insert_temperature
from src.database.humidity import insert_humidity

def generate_test_data():
    min_temperature, max_temperature = 15.0, 40.0
    min_humidity, max_humidity = 30.0, 90.0

    end_date = datetime.now()
    start_date = end_date - timedelta(days=3*365)

    current_date = start_date
    while current_date <= end_date:
        temperature = round(random.uniform(min_temperature, max_temperature), 2)
        humidity = round(random.uniform(min_humidity, max_humidity), 2)

        temperature_alert = 1 if temperature > 30 else 0
        humidity_alert = 1 if humidity > 70 else 0

        insert_temperature(temperature, temperature_alert, current_date)
        insert_humidity(humidity, humidity_alert, current_date)

        current_date += timedelta(days=1)

    print("População de dados fakes concluída.")

