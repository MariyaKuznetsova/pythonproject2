import re
from datetime import datetime
from src.masks import get_mask_account, get_mask_card_number
from src.process_bank import process_bank_search
from src.trans_read import excel_func, func_csv_
from src.utils import operation_func


def number_transaction_func():
    """Функция получения списка транзакций из файла"""
    while True:
        number_transaction = int(input("Введите выбранный пункт меню: "))
        if number_transaction == 1:
            print('Для обработки выбран JSON-файл')
            data = operation_func("data/operations.json")
            return data
        elif number_transaction == 2:
            print('Для обработки выбран CSV-файл')
            data = func_csv_("data/transactions.csv")
            return data
        elif number_transaction == 3:
            print('Для обработки выбран XLSX-файл')
            data = excel_func("data/transactions_excel.xlsx")
            return data
        else:
            continue


# def process_bank_search_1(data: list[dict]) -> list[dict]:
#     """Функция операции фильтрации по статусу"""
#
#     #pattern = search
#     #search = "EXECUTED"
#     #print(data)
#     try:
#         dict_new = []
#         search = "EXECUTED"
#         for operation in data:
#             if operation['state'] == search:
#                 dict_new.append(operation)
#             else:
#                 continue
#         #print(dict_new)
#         return dict_new
#     except Exception:
#         return []


def transaction_status_func(data: list[dict]) -> list[dict]:
    """Функция сортировки транзакций по статусу"""
    print()
    while True:
        print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")
        print()
        transaction_status = str(input("Введите выбранный статус: "))
        search = transaction_status.upper()
        print()
        if search in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f'Операции отфильтрованы по статусу "{search}"')
            break
        else:
            print(f'Статус операции "{search}" недоступен.')
            continue
    data_search_1 = process_bank_search(data, search)
    print(data_search_1)
    return data_search_1


def sort_transaction_func(data_search: list[dict], reverse=False) -> list[dict]:
    """Функция сортировки по дате"""
    sort_transaction = str(input("Введите ответ: "))
    if sort_transaction.lower() == "по возрастанию":
        sorted_data_search_answer = sorted(data_search, key=lambda data_search: data_search["date"], reverse=False)
        return sorted_data_search_answer
    elif sort_transaction.lower() == "по убыванию":
        sorted_data_search_answer = sorted(data_search, key=lambda data_search: data_search["date"], reverse=True)
        return sorted_data_search_answer


def transaction_date_func(data_search: list[dict]) -> list[dict]:
    """Функция сортировки транзакций по дате"""
    print()
    print("Отсортировать операции по дате? Да/Нет")
    data_transaction = str(input("Введите ответ: "))
    if data_transaction.capitalize() == "Да":
        print("Отсортировать по возрастанию или по убыванию?")
        sorted_data_search = sort_transaction_func(data_search)
        return sorted_data_search
    elif data_transaction.capitalize() == "Нет":
        sorted_data_search = data_search
        return sorted_data_search


def process_bank_search_rub(sorted_data_search: list[dict], search="RUB") -> list[dict]:
    """Функция операции сортировки транзакций по валюте"""
    dict_new = []
    pattern = search
    try:
        for operation in sorted_data_search:
            if re.search(
                pattern,
                operation["currency_code"] or operation["operationAmount"]["currency"]["code"],
                flags=re.IGNORECASE,
            ):
                dict_new.append(operation)
            else:
                continue
        return dict_new
    except Exception:
        return []


def transaction_date_func_rub(sorted_data_search: list[dict]) -> list[dict]:
    """Функция сортировки транзакций по валюте"""
    print()
    print("Выводить только рублевые транзакции? Да/Нет")
    rub_transaction = str(input("Введите ответ: "))
    if rub_transaction.capitalize() == "Да":
        sorted_data_search_tr = process_bank_search_rub(sorted_data_search)
        return sorted_data_search_tr
    elif rub_transaction.capitalize() == "Нет":
        sorted_data_search_tr = sorted_data_search
        return sorted_data_search_tr


def transaction_date_func_word(sorted_data_search_tr: list[dict]) -> list[dict]:
    """Функция сортировки транзакций по определенному слову в описании"""
    print()
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    fil_transaction = str(input("Введите ответ: "))
    if fil_transaction.capitalize() == "Да":
        print("Введите описание транзакции: ")
        fil_transaction_word = str(input())
        fil_transaction_new = process_bank_search(sorted_data_search_tr, fil_transaction_word)
        return fil_transaction_new
    elif fil_transaction.capitalize() == "Нет":
        fil_transaction_new = sorted_data_search_tr
        return fil_transaction_new


def account_from_to_card(text: str) -> str:
    """Функция для операций с картой"""
    pattern = re.compile(r"\s+")
    split_text_1 = pattern.split(text)
    text_1 = get_mask_card_number(split_text_1[-1])
    text_2 = split_text_1[:-1]
    text_2_str = " ".join(text_2)
    return f"{text_2_str} {text_1}"


def account_from_to(text: str) -> str:
    """Функция для операций со счетом"""
    pattern = re.compile(r"\s+")
    split_text_1 = pattern.split(text)
    text_check_1 = get_mask_account(split_text_1[-1])
    return f"Счет {text_check_1}"


def main():
    """Сборка всех функций в приложение"""
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    print()
    data = number_transaction_func()
    print(data)
    data_search = transaction_status_func(data)
    print(data_search)
    sorted_data_search = transaction_date_func(data_search)
    print(sorted_data_search)
    sorted_data_search_tr = transaction_date_func_rub(sorted_data_search)
    print(sorted_data_search_tr)
    fil_transaction_new = transaction_date_func_word(sorted_data_search_tr)
    print(fil_transaction_new)
    print()
    print("Распечатываю итоговый список транзакций...")
    print()
    trans_count = 0
    for trans in fil_transaction_new:
        trans_count += 1
    if trans_count == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    elif trans_count > 0:
        print(f"Всего банковских операций в выборке: {trans_count}")
        print()
        for tr in fil_transaction_new:
            date_string = tr["date"]
            date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")
            date = date_obj.strftime("%d.%m.%Y")
            description = tr["description"]
            amount = tr["amount"]
            currency = tr["currency_code"]
            if tr["description"] == "Открытие вклада":
                account = account_from_to(tr["to"])
                print(f"{date} {description}\n{account}\nСумма: {amount} {currency}\n")
            elif tr["description"] == "Перевод с карты на карту":
                text__1 = tr["from"]
                text__2 = tr["to"]
                account_1 = account_from_to_card(text__1)
                account_2 = account_from_to_card(text__2)
                print(f"{date} {description}\n{account_1} -> {account_2}\nСумма: {amount} {currency}\n")
            elif tr["description"] == "Перевод организации":
                text__3 = tr["from"]
                text__4 = tr["to"]
                if text__3[:4] == "Счет":
                    account_3 = account_from_to(text__3)
                    if text__4[:4] == "Счет":
                        account_4 = account_from_to(text__4)
                    elif text__4[:4] != "Счет":
                        account_4 = account_from_to_card(text__4)
                elif text__3[:4] != "Счет":
                    account_3 = account_from_to_card(text__3)
                    if text__4[:4] == "Счет":
                        account_4 = account_from_to(text__4)
                    elif text__4[:4] != "Счет":
                        account_4 = account_from_to_card(text__4)
                print(f"{date} {description}\n{account_3} -> {account_4}\nСумма: {amount} {currency}\n")
            elif tr["description"] == "Перевод со счета на счет":
                account_5 = account_from_to(tr["from"])
                account_6 = account_from_to(tr["to"])
                print(f"{date} {description}\n{account_5} -> {account_6}\nСумма: {amount} {currency}\n")


main()
