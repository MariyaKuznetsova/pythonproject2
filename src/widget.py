def mask_account_card(b: [str]) -> [str]:
    details_card = input("Введите данные: ")
    details_card_splits = details_card.split(" ")
    if details_card_splits[0] == "Счет":
        print(details_card_splits[1])
    else:
        print(f'{details_card_splits[0:2]}')
        #from masks import get_mask_account
        #print(get_mask_account(details_card_splits[1]))
    #name_card = details_card_splits.isalpha()
    #details_card_new = f'{details_card_splits.isalpha()} {masks.get_mask_card_number(details_card_splits.isdigit())} '
    #print(name_card)

mask_account_card([str])


#datetime.strptime
#strftime