import logging
from typing import Union


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.debug(f"Выполняется функция маскировки номера банковской карты: {'get_mask_card_number'}")


def get_mask_card_number(number_card: Union[str]) -> Union[str]:
    """Функцию маскировки номера банковской карты"""
    try:
        logger.info(f"Выполняется функция c номером карты: {number_card}")
        if number_card == " ":
            logger.warning(f"Номер карты указан неправильно {number_card}")
            return "Отсутствует номер карты"
        else:
            logger.info(f"Выполняется маскировка номера карты: {number_card}")
            number_card_new = f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[12:]}"
            logger.debug(f"Произведена маскировка номера карты: {number_card_new}")
            return number_card_new
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


number_card = " "
get_mask_card_number(number_card)

logger.debug(f"Выполняется функция маскировки номера банковского счета: {'get_mask_account'}")


def get_mask_account(number_check: Union[str]) -> Union[str]:
    """Функцию маскировки номера банковского счета"""
    try:
        logger.info(f"Выполняется функция c номером банковского счета: {number_check}")
        if number_check == " ":
            logger.warning(f"Номер банковского счета указан неправильно {number_check}")
            return "Отсутствует номер счета"
        else:
            logger.info(f"Выполняется маскировка номера банковского счета: {number_check}")
            number_check_new_s = f"**{number_check[15:]}"
            logger.debug(f"Произведена маскировка номера банковского счета: {number_check_new_s}")
            return number_check_new_s
    except Exception as ex:
        logger.error(f"Произошла ошибка: {ex}")


number_check = "9848418484941515151895684"
get_mask_account(number_check)
