import os
from typing import Dict

import requests
from dotenv import load_dotenv

"""Загружаем API ключ в окружение"""
load_dotenv(".env")
"""Читаем API ключ из окружения"""
API_KEY = os.getenv("API_KEY")


def convert_func(transactions: Dict) -> float:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    amount_code = transactions.get("operationAmount", {}).get("currency", {}).get("code")
    if amount_code == "RUB":
        amount = transactions.get("operationAmount", {}).get("amount", {})
        amount_float = float(amount)
        return amount_float
    else:
        amount_currency = transactions.get("operationAmount", {}).get("amount", {})
        url = f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}"
        response = requests.get(url)
        repos = response.json()
        answer = repos.get("rates")
        answer_rub = answer.get("RUB")
        amount_currency_float = float(amount_currency)
        answer_rub_float = answer_rub * amount_currency_float
        return answer_rub_float
