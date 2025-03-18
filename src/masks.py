def get_mask_card_number(number_card: [str]) -> [str]:
    """Функцию маскировки номера банковской карты"""
    #number_card = input("Введите номер карты  ")
    number_card_new = f'{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:]}'
    return number_card_new

number_card = "1596837868705199"
get_mask_card_number(number_card)


def get_mask_account(number_check: [str]) -> [str]:
    """Функцию маскировки номера банковского счета"""
    #number_check = input("Введите номер счета  ")
    number_check_new_s = f'**{number_check[15:]}'
    return number_check_new_s

number_check = "35383033474447895560"
get_mask_account(number_check)
