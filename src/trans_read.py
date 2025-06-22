import csv
from typing import Dict, List, Union

import pandas as pd


def func_csv_(csv_file: Union[str]) -> List[Dict]:
    """Функция для считывания финансовых операций из CSV"""
    try:
        with open(csv_file, encoding="utf-8") as trans_file:
            reader = csv.DictReader(trans_file, delimiter=";")
            list_dictionary = []
            for row in reader:
                list_dictionary.append(row)
            return list_dictionary
    except Exception:
        return []


print(func_csv_("transactions.csv"))


def excel_func(excel_file: Union[str]) -> List[Dict]:
    """Функция для считывания финансовых операций из Excel"""
    try:
        excel_trans = pd.read_excel(excel_file)
        dictionary = excel_trans.to_dict("records")
        return dictionary
    except Exception:
        return []


print(excel_func("../data/transactions_excel.xlsx"))
