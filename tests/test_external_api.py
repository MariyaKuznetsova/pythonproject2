import os
from unittest.mock import Mock, patch

import pytest
from dotenv import load_dotenv

from src.external_api import convert_func

load_dotenv(".env")
API_KEY = os.getenv("API_KEY")


@patch("requests.get")
def test_convert_func(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 78.496243}}
    assert (
        convert_func(
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
            }
        )
        == 645346.6573129101
    )
    mock_get.assert_called_with(f"https://openexchangerates.org/api/latest.json?app_id={API_KEY}")


def test_convert_func_1():
    mock_transactions = Mock(return_value=43.3)
    convert_func = mock_transactions
    assert convert_func() == 43.3
    mock_transactions.assert_called_with()
