def get_mask_card_number(number_card: [str]) -> [str]:
    """Функцию маскировки номера банковской карты"""
    #number_card = input("Введите номер карты  ")
    number_card_new = f'{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:]}'
    print(number_card_new)

number_card = "84281762182468118"
get_mask_card_number(number_card)


def get_mask_account(number_check: [str]) -> [str]:
    """Функцию маскировки номера банковского счета"""
    #number_check = input("Введите номер счета  ")
    number_check_new_s = f'**{number_check[15:]}'
    print(number_check_new_s)

number_check = "88718421712982152848"
get_mask_account(number_check)
