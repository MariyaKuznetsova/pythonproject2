from typing import Dict, List, Union


def filter_by_currency(transactions: List[Dict], currency: Union[str]) -> List[Dict]:
    """Функция возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной."""
    try:
        for i in transactions:
            if i["operationAmount"]["currency"]["code"] == currency:
                yield i
            elif i["operationAmount"]["currency"]["code"] != currency:
                continue
    except Exception:
        print("Неправильный формат данных")


def transaction_descriptions(transactions: List[Dict]) -> List[Dict]:
    """Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    try:
        for i in transactions:
            yield i["description"]
    except Exception:
        print("Неправильный формат данных")


def card_number_generator(start: int, stop: int) -> int:
    """Генератор, который выдает номера банковских карт в формате
    XXXX XXXX XXXX XXXX. start - начало диапазона, stop - конец диапазона"""
    while start <= stop:
        number = f"{start:016d}"
        yield f"{number[0:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        start += 1
        if stop > 9999999999999999:
            stop == 9999999999999999
    else:
        print("Неправильный формат данных")
