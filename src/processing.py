from typing import List, Dict


def filter_by_state(dictionary: List[Dict], state: str) -> List[Dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    new_filter = []
    for by_states in dictionary:
        if by_states.get("state") == state:
            new_filter.append(by_states)
    return new_filter


def sort_by_date(dictionary_date: List[Dict], reverse=True) -> List[Dict]:
    """Функция сортировки списка словарей по дате"""
    sorted_dictionary_date = sorted(dictionary_date, key=lambda product: product["date"], reverse=True)
    return sorted_dictionary_date
