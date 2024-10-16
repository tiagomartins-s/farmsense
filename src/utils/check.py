from src.utils.log import record_log

def status(temperature, humidity):
    if temperature > 30 and humidity < 40:
        print("É recomendado irrigar a plantação!")
        record_log("Sistema recomendou irrigar a plantação.")
    elif temperature < 30 and humidity > 70:
        print("É recomendado que a irrigação seja suspensa!")
        record_log("Sistema recomendou suspender irrigação.")
    elif temperature > 30:
        record_log("Sistema gerou alerta para estresse hídrico.")
        print("Alerta para estresse hídrico!")
    elif humidity > 70:
        record_log("Sistema gerou alerta para doenças fúngicas.")
        print("Alerta para risco de doenças fúngicas!")
    else:
        record_log("Sistema indicou parametros dentro do esperado.")
        print("Os sensores indicam temperatura e umidade ideais.")

def check_temperature(temperature):
    alert = 0
    if temperature > 30:
        print("Alerta para estresse hídrico.")
        alert = 1
    return alert

def check_humidity(humidity):
    alert = 0
    if humidity > 70:
        print("Alerta para risco de doenças fúngicas.")
        alert = 1
    return alert