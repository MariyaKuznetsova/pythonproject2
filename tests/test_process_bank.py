from collections import Counter

import pytest

from src.process_bank import process_bank_operations, process_bank_search

data = [
    {
        "id": 441945886,
        "state": "CANCELED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    },
    {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    },
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 587085106,
        "state": "PENDING",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
]


def test_process_bank_search():
    assert process_bank_search(data, "PENDING") == [
        {
            "id": 587085106,
            "state": "PENDING",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_process_bank_search_1():
    assert process_bank_search([], "PENDING") == []


@pytest.fixture
def examples_process_bank_search():
    return [
        {
            "id": 587085106,
            "state": "PENDING",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        }
    ]


def test_process_bank_search_2(examples_process_bank_search):
    assert process_bank_search(data, "PENDING") == examples_process_bank_search


@pytest.mark.parametrize(
    "list_value_search, value_search, function_output",
    [
        (
            data,
            "PENDING",
            [
                {
                    "id": 587085106,
                    "state": "PENDING",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431",
                }
            ],
        ),
        (
            data,
            "EXECUTED",
            [
                {
                    "id": 41428829,
                    "state": "EXECUTED",
                    "date": "2019-07-03T18:35:29.512364",
                    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "MasterCard 7158300734726758",
                    "to": "Счет 35383033474447895560",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
            ],
        ),
        ([], "EXECUTED", []),
        (
            data,
            "CANCELED",
            [
                {
                    "id": 441945886,
                    "state": "CANCELED",
                    "date": "2019-08-26T10:50:58.294041",
                    "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Maestro 1596837868705199",
                    "to": "Счет 64686473678894779589",
                }
            ],
        ),
    ],
)
def test_process_bank_search_3(list_value_search, value_search, function_output):
    assert process_bank_search(list_value_search, value_search) == function_output


def test_process_bank_operations():
    assert process_bank_operations(data, ["Открытие вклада"]) == Counter({"Открытие вклада": 1})


def test_process_bank_operations_1():
    assert process_bank_operations([], ["Открытие вклада"]) == Counter()


@pytest.fixture
def examples_process_bank_operations():
    return Counter({"Открытие вклада": 1})


def test_process_bank_operations_2(examples_process_bank_operations):
    assert process_bank_operations(data, ["Открытие вклада"]) == examples_process_bank_operations


@pytest.mark.parametrize(
    "list_value_operations, value_operations, function_output_operations",
    [
        (data, ["Открытие вклада"], Counter({"Открытие вклада": 1})),
        (
            data,
            ["Перевод организации", "Открытие вклада", "Перевод со счета на счет"],
            Counter({"Перевод организации": 3, "Открытие вклада": 1, "Перевод со счета на счет": 1}),
        ),
        ([], ["Открытие вклада"], Counter()),
        (
            data,
            ["Перевод организации", "Перевод со счета на счет"],
            Counter({"Перевод организации": 3, "Перевод со счета на счет": 1}),
        ),
    ],
)
def test_process_bank_operations_3(list_value_operations, value_operations, function_output_operations):
    assert process_bank_operations(list_value_operations, value_operations) == function_output_operations
