from typing import Union


def get_mask_card_number(a: Union[int]) -> Union[int]:
    """Функцию маскировки номера банковской карты"""
    number_card = list(input("Введите номер карты  "))
    first_seven_number = number_card[0:6]
    number_card[6:12] = ["*", "*", "*", "*", "*", "*"]
    two_six_number = number_card[6:12]
    tree_four_number = number_card[12:]
    number_card_new = first_seven_number + two_six_number + tree_four_number
    number_card_new.insert(4, " ")
    number_card_new.insert(9, " ")
    number_card_new.insert(14, " ")
    number_card_new_s = "".join(number_card_new)
    print(number_card_new_s)


get_mask_card_number()


def get_mask_account(a: Union[int]) -> Union[int]:
    """Функцию маскировки номера банковского счета"""
    number_check = list(input("Введите номер счета  "))
    tree_four_check = number_check[15:]
    tree_four_check[0:1] = ["*", "*"]
    number_check_new_s = "".join(tree_four_check)
    print(number_check_new_s)


get_mask_account()
