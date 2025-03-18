def mask_account_card(details_card: [str]) -> [str]:
    details_card_splits = details_card.split(" ")
    from masks import get_mask_account
    from masks import get_mask_card_number
    if details_card_splits[0] == "Счет":
        print(f"{details_card_splits[0]} {get_mask_account(details_card_splits[1])}")
    else:
        if details_card_splits[0] == "Visa":
            print(f"{details_card_splits[0]} {details_card_splits[1]} {get_mask_card_number(details_card_splits[-1])}")
        else:
            print(f"{details_card_splits[0]} {get_mask_card_number(details_card_splits[-1])}")


details_card = "Счет 73654108430135874305"
mask_account_card(details_card)

def get_date(date_str: [str]) -> [str]:
    date_new = f'"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"'
    print(date_new)


date_str = "2024-03-11T02:26:18.671407"
get_date(date_str)