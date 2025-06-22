import json
import logging
import os
from typing import Dict, List, Union

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
os.makedirs("../logs", exist_ok=True)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.debug(f"Выполняется функция: {'operation_func'}")


def operation_func(operations_file: Union[str] | Dict) -> List[Dict]:
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях"""
    try:
        logger.info(f"Выполняется функция преобразования файла {'operations_file'}")
        with open(operations_file, encoding="utf-8") as f:
            operations = json.load(f)
            logger.info(f"Выполняется преобразование JSON-файла {'operations_file'} в список словарей")
            return operations
    except json.JSONDecodeError as ex:
        logger.error(f"Произошла ошибка: {ex}")
        return []


# operation_func("../data/operations.json")
