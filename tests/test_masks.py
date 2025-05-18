import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number():
    assert get_mask_card_number("1848494151515189") == "1848 49** **** 5189"


def test_get_mask_card_number_two():
    assert get_mask_card_number("18484941515151895684") == "1848 49** **** 51895684"


def test_get_mask_card_number_tree():
    assert get_mask_card_number("1848491895684") == "1848 49** **** 4"


def test_get_mask_card_number_four():
    assert get_mask_card_number(" ") == "Отсутствует номер карты"


@pytest.fixture
def examples_of_values1():
    return "1848 49** **** 51895684"


@pytest.fixture
def examples_of_values2():
    return "8949 68** **** 484"


@pytest.fixture
def examples_of_values3():
    return "2846 21** **** 62432"


@pytest.fixture
def examples_of_values4():
    return "1848 78** **** 444"


def test_get_mask_card_number_five1(examples_of_values1):
    assert get_mask_card_number("18484941515151895684") == examples_of_values1


def test_get_mask_card_number_five2(examples_of_values2):
    assert get_mask_card_number("894968413848484") == examples_of_values2


def test_get_mask_card_number_five3(examples_of_values3):
    assert get_mask_card_number("28462175387962432") == examples_of_values3


def test_get_mask_card_number_five4(examples_of_values4):
    assert get_mask_card_number("184878648644444") == examples_of_values4


@pytest.mark.parametrize(
    "entering_a_value, function_output",
    [
        ("18484941515151895684", "1848 49** **** 51895684"),
        ("894968413848484", "8949 68** **** 484"),
        ("28462175387962432", "2846 21** **** 62432"),
        ("184878648644444", "1848 78** **** 444"),
    ],
)
def test_get_mask_card_number_six(entering_a_value, function_output):
    assert get_mask_card_number(entering_a_value) == function_output


def test_get_mask_account():
    assert get_mask_account("64644981848494151515189") == "**51515189"


def test_get_mask_account_two():
    assert get_mask_account("69848418484941515151895684") == "**15151895684"


def test_get_mask_account_tree():
    assert get_mask_account("18486448491895684") == "**84"


def test_get_mask_account_four():
    assert get_mask_account(" ") == "Отсутствует номер счета"


@pytest.fixture
def examples_of_values_account1():
    return "**51515189"


@pytest.fixture
def examples_of_values_account2():
    return "**5151895684"


@pytest.fixture
def examples_of_values_account3():
    return "**84"


@pytest.fixture
def examples_of_values_account4():
    return "**32652"


def test_get_mask_account_five1(examples_of_values_account1):
    assert get_mask_account("64644981848494151515189") == examples_of_values_account1


def test_get_mask_account_five2(examples_of_values_account2):
    assert get_mask_account("9848418484941515151895684") == examples_of_values_account2


def test_get_mask_account_five3(examples_of_values_account3):
    assert get_mask_account("18486448491895684") == examples_of_values_account3


def test_get_mask_account_five4(examples_of_values_account4):
    assert get_mask_account("26848174636241832652") == examples_of_values_account4


@pytest.mark.parametrize(
    "entering_a_value_account, function_output_account",
    [
        ("64644981848494151515189", "**51515189"),
        ("9848418484941515151895684", "**5151895684"),
        ("18486448491895684", "**84"),
        ("26848174636241832652", "**32652"),
    ],
)
def test_get_mask_account_six(entering_a_value_account, function_output_account):
    assert get_mask_account(entering_a_value_account) == function_output_account
