from fastapi import FastAPI
import requests

app = FastAPI()

# Вставь сюда свой реальный API-ключ
api_key = 'ee7d76b1eacfb053d967bdde'
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

@app.get("/convert")
def convert(amount: float, from_currency: str, to_currency: str):
    response = requests.get(url)
    data = response.json()  # Получаем курсы валют
    
    # Проверяем, что курсы получены
    if 'conversion_rates' not in data:
        return {"error": "Не удалось получить курсы валют"}
    
    rates = data['conversion_rates']
    
    if from_currency == "USD":
        # Конвертируем из USD в целевую валюту
        if to_currency in rates:
            converted_amount = amount * rates[to_currency]
            return {"converted_amount": converted_amount}
    elif from_currency in rates and to_currency in rates:
        # Конвертируем между другими валютами
        from_rate = rates[from_currency]
        to_rate = rates[to_currency]
        converted_amount = amount * (to_rate / from_rate)
        return {"converted_amount": converted_amount}
    
    return {"error": "Неверные валюты"}