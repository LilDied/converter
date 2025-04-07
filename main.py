from fastapi import FastAPI

app = FastAPI()

rates = {
    "USD": {
        "BYN": 3.27018,  # 1 USD = 3.27018 BYN
        "EUR": 0.91683,  # 1 USD = 0.91683 EUR
        "RUB": 86.1350,  # 1 USD = 86.1350 RUB
        "USD": 1
    },
    "BYN": {
        "USD": 0.305808,  # 1 BYN = 0.305808 USD
        "EUR": 0.279637,  # 1 BYN = 0.279637 EUR
        "RUB": 25.7930,  # 1 BYN = 25.7930 RUB
        "BYN": 1
    },
    "EUR": {
        "USD": 1.09071,  # 1 EUR = 1.09071 USD
        "BYN": 3.5760,   # 1 EUR = 3.5760 BYN
        "RUB": 94.0,     # 1 EUR = 94.0 RUB
        "EUR": 1
    },
    "RUB": {
        "USD": 0.01161,  # 1 RUB = 0.01161 USD
        "BYN": 0.03876,  # 1 RUB = 0.03876 BYN
        "EUR": 0.01064,  # 1 RUB = 0.01064 EUR
        "RUB": 1
    }
}

@app.get("/convert")
def convert(from_currency: str, to_currency: str, amount: float):
    try:
        rate = rates[from_currency.upper()][to_currency.upper()]
        converted_amount = amount * rate
        return {
            "from": from_currency.upper(),
            "to": to_currency.upper(),
            "amount": amount,
            "converted": round(converted_amount, 2)
        }
    except KeyError:
        return {"error": "Валюта не найдена или неверно введена"}



