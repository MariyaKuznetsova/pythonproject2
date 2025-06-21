from unittest.mock import Mock, mock_open, patch

import pytest
import src.utils


def test_operation_func():
    mock_operations_file = Mock(
        return_value=[
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        ]
    )
    operation_func = mock_operations_file
    assert operation_func() == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    mock_operations_file.assert_called_with()


@patch(
    "src.utils.open",
    new_callable=mock_open,
    read_data='[{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364", "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}}}]',
)
def test_operation_func_1(mock_operations_file):
    result_1 = src.utils.operation_func("../data/expected_result_test.json")
    assert result_1 == [
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        }
    ]
    mock_operations_file.assert_called_with("../data/expected_result_test.json", encoding="utf-8")
