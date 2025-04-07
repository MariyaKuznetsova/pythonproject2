from typing import Union


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функцию маскировки номера банковской карты"""
    if number_card == " ":
        return "Отсутствует номер карты"
    else:
        number_card_new = f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:]}"
        return number_card_new


# number_card = "184878648644444"
# get_mask_card_number(number_card)


def get_mask_account(number_check: Union[str]) -> Union[str]:
    """Функцию маскировки номера банковского счета"""
    if number_check == " ":
        return "Отсутствует номер счета"
    else:
        number_check_new_s = f"**{number_check[15:]}"
        return number_check_new_s


# number_check = "9848418484941515151895684"
# get_mask_account(number_check)
