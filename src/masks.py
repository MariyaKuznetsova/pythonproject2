def get_mask_card_number(a: [str]) -> [str]:
    """Функцию маскировки номера банковской карты"""
    number_card = input("Введите номер карты  ")
    number_card_new = f'{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:]}'
    print(number_card_new)


get_mask_card_number([str])


def get_mask_account(a: [str]) -> [str]:
    """Функцию маскировки номера банковского счета"""
    number_check = input("Введите номер счета  ")
    number_check_new_s = f'**{number_check[15:]}'
    print(number_check_new_s)


get_mask_account([str])
