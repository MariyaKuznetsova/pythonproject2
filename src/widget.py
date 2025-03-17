import masks

def mask_account_card(a: [str]) -> [str]:
    details_card = input("Введите данные: ")
    details_card_splits = details_card.split(" ")
    print(details_card_splits)
    details_card_new = f'{details_card_splits.isdigit()} {masks.get_mask_card_number(details_card_splits.isdigit())} '
    print(details_card_new)

mask_account_card([str])
