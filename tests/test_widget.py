from src.widget import mask_account_card

from src.widget import get_date

import pytest


def test_mask_account_card():
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


def test_mask_account_card_two():
    assert mask_account_card("Счет 64686473678894779589") == "Счет **79589"


def test_mask_account_card_tree():
    assert mask_account_card("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"


def test_mask_account_card_four():
    assert mask_account_card(" ") == "Неправильный формат данных"


@pytest.fixture
def examples_mask_card1():
    return "Счет **95560"


@pytest.fixture
def examples_mask_card2():
    return "Visa Classic 6831 98** **** 7658"


@pytest.fixture
def examples_mask_card3():
    return "Visa Platinum 8990 92** **** 5229"


@pytest.fixture
def examples_mask_card4():
    return "Visa Gold 5999 41** **** 6353"


def test_mask_account_card_five1(examples_mask_card1):
    assert mask_account_card("Счет 35383033474447895560") == examples_mask_card1


def test_mask_account_card_five2(examples_mask_card2):
    assert mask_account_card("Visa Classic 6831982476737658") == examples_mask_card2


def test_mask_account_card_five3(examples_mask_card3):
    assert mask_account_card("Visa Platinum 8990922113665229") == examples_mask_card3


def test_mask_account_card_five4(examples_mask_card4):
    assert mask_account_card("Visa Gold 5999414228426353") == examples_mask_card4


@pytest.mark.parametrize(
    "entering_mask_card, function_output_mask_card",
    [
        ("Счет 353830334744478955601515", "Счет **955601515"),
        (" ", "Неправильный формат данных"),
        ("Счет 353830334744256125", "Счет **125"),
        ("Visa Gold 599941422842635384882", "Visa Gold 5999 41** **** 635384882"),
    ],
)
def test_mask_account_card_six(entering_mask_card, function_output_mask_card):
    assert mask_account_card(entering_mask_card) == function_output_mask_card


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == '"11.03.2024"'


def test_get_date_two():
    assert get_date("2020-06-21T857698472984TGY") == '"21.06.2020"'


def test_get_date_tree():
    assert get_date("202021T857698472984TGY") == "Неправильный формат данных"


def test_get_date_four():
    assert get_date(" ") == "Неправильный формат данных"


@pytest.fixture
def examples_get_date1():
    return '"05.10.1993"'


@pytest.fixture
def examples_get_date2():
    return '"03.04.1093"'


@pytest.fixture
def examples_get_date3():
    return "Неправильный формат данных"


@pytest.fixture
def examples_get_date4():
    return "Неправильный формат данных"


def test_get_date_five1(examples_get_date1):
    assert get_date("1993-10-0521T8") == examples_get_date1


def test_get_date_five2(examples_get_date2):
    assert get_date("1093-04-03thsytrbtn57827") == examples_get_date2


def test_get_date_five3(examples_get_date3):
    assert get_date("209307-01vtbnay5syn6732") == examples_get_date3


def test_get_date_five4(examples_get_date4):
    assert get_date("ywsn56u626848174636241832652") == examples_get_date4


@pytest.mark.parametrize(
    "entering_get_date, function_output_get_date",
    [
        (" ", "Неправильный формат данных"),
        ("2025-04-01T02:26:18.653543", '"01.04.2025"'),
        ("2000-08-05T02:26:18.653543", '"05.08.2000"'),
        ("26848174636241832652", "Неправильный формат данных"),
    ],
)
def test_get_date_six(entering_get_date, function_output_get_date):
    assert get_date(entering_get_date) == function_output_get_date
