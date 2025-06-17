import json
from typing import Dict, List, Union


def operation_func(operations_file: Union[str] | Dict) -> List[Dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(operations_file, encoding="utf-8") as f:
            operations = json.load(f)
            return operations
    except json.JSONDecodeError:
        return []
