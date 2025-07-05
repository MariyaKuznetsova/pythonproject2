from unittest.mock import Mock, mock_open, patch

import pandas as pd

import src.trans_read
from src.trans_read import excel_func


def test_func_csv_():
    mock_csv_file = Mock(
        return_value=[
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    func_csv_ = mock_csv_file
    assert func_csv_() == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_csv_file.assert_called_with()


@patch(
    "src.trans_read.open", new_callable=mock_open, read_data="id;state;date\n650703;EXECUTED;2023-09-05T11:30:32Z\n"
)
def test_func_csv_1(mock_csv_file):
    result_func_1 = src.trans_read.func_csv_("../data/trans_read_test.csv")
    assert result_func_1 == [{"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}]
    mock_csv_file.assert_called_with("../data/trans_read_test.csv", encoding="utf-8")


@patch("src.trans_read.open", new_callable=mock_open, read_data=" ")
def test_func_csv_2(mock_csv_file):
    result_func_2 = src.trans_read.func_csv_(" ")
    assert result_func_2 == []
    mock_csv_file.assert_called_with(" ", encoding="utf-8")


def test_excel_func():
    mock_excel_file = Mock(
        return_value=[
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
    )
    excel_func = mock_excel_file
    assert excel_func() == [
        {
            "id": "650703",
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": "16210",
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]
    mock_excel_file.assert_called_with()


@patch("pandas.read_excel")
def test_excel_func_1(mock_excel_file):
    mock_excel_file.return_value = pd.DataFrame([{"id": 650703, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}])
    assert excel_func("../data/transactions_excel_test.xlsx") == [
        {"id": 650703, "state": "EXECUTED", "date": "2023-09-05T11:30:32Z"}
    ]
    mock_excel_file.assert_called_with("../data/transactions_excel_test.xlsx")


@patch("pandas.read_excel")
def test_excel_func_2(mock_excel_file):
    mock_excel_file.return_value = pd.DataFrame([])
    assert excel_func(" ") == []
    mock_excel_file.assert_called_with(" ")
