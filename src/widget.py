from typing import Union


def mask_account_card(details_card: Union[str]) -> Union[str]:
    """Функцию вывода номера карты или счета с функцией маскировки"""
    details_card_splits = details_card.split(" ")
    from src.masks import get_mask_account, get_mask_card_number
    if details_card_splits[0] == "Счет":
        return f"{details_card_splits[0]} {get_mask_account(details_card_splits[1])}"
    else:
        if details_card_splits[0] == "Visa":
            return f"{details_card_splits[0]} {details_card_splits[1]} {get_mask_card_number(details_card_splits[-1])}"
        else:
            return f"{details_card_splits[0]} {get_mask_card_number(details_card_splits[-1])}"


details_card = "Счет 73654108430135874305"
print(mask_account_card(details_card))


def get_date(date_str: Union[str]) -> Union[str]:
    """Функцию преобразования строки в строку с датой"""
    date_new = f'"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"'
    return date_new


date_str = "2024-03-11T02:26:18.671407"
print(get_date(date_str))
