"""
@file storage.py
@brief Модуль сохранения и загрузки расходов в JSON-файл.

Работает с файлом expenses.json в текущей директории.
"""

import json
import os

FILE_NAME = "expenses.json"
"""
@brief Имя файла для хранения расходов.

Расположен в текущей рабочей директории.
"""


def load_expenses():
    """
    @brief Загрузить расходы из файла.

    @return Список словарей с расходами. Если файла нет — пустой список.
    """
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_expenses(expenses):
    """
    @brief Сохранить расходы в файл.

    @param expenses Список словарей с расходами.

    @note Данные пишутся в UTF-8 без экранирования кириллицы (ensure_ascii=False)
          с отступом 2 для читаемости.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)