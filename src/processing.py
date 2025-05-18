from typing import Dict, List

from mypy.types import AnyType


def filter_by_state(dictionary: List[Dict], state: AnyType) -> List[Dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    try:
        new_filter = []
        for by_states in dictionary:
            if by_states.get("state") == state:
                new_filter.append(by_states)
        return new_filter
    except:
        return []


def sort_by_date(dictionary_date: List[Dict], reverse: AnyType) -> List[Dict]:
    """Функция сортировки списка словарей по дате"""
    try:
        if reverse == False:
            sorted_dictionary_date = sorted(dictionary_date, key=lambda product: product["date"], reverse=False)
            return sorted_dictionary_date
        elif reverse == True:
            sorted_dictionary_date = sorted(dictionary_date, key=lambda product: product["date"], reverse=True)
            return sorted_dictionary_date
    except:
        return "Неверный формат данных"
