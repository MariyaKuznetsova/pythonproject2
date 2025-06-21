import csv
from typing import Dict, List, Union

import pandas as pd


def func_csv_(csv_file: Union[str]) -> List[Dict]:
    try:
        with open(csv_file, encoding="utf-8") as trans_file:
            reader = csv.DictReader(trans_file, delimiter=";")
            list_dictionary = []
            for row in reader:
                list_dictionary.append(row)
            return list_dictionary
    except Exception:
        return []


#print(func_csv_("../data/trans_read_test.csv"))


def excel_func(excel_file: Union[str]) -> List[Dict]:
    try:
        excel_trans = pd.read_excel(excel_file)
        dictionary = excel_trans.to_dict("records")
        return dictionary
    except Exception:
        return []


#print(excel_func("../data/transactions_excel_test.xlsx"))
