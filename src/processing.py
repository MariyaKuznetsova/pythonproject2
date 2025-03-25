from typing import List, Dict


def filter_by_state(dictionary: List[Dict]) -> List[Dict]:
    """Функция возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению"""
    new_filter = []
    for by_states in dictionary:
        if by_states.get("state") == value_states:
            new_filter.append(by_states)
    return new_filter


value_states = "EXECUTED"
dictionary = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
print(filter_by_state(dictionary))


def sort_by_date(dictionary_date: List[Dict]) -> List[Dict]:
    """Функция сортировки списка словарей по дате"""
    sorted_dictionary_date = sorted(dictionary_date, key=lambda product: product["date"], reverse=True)
    return sorted_dictionary_date


dictionary_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.4109441"},
]
print(sort_by_date(dictionary_date))
