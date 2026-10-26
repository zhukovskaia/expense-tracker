"""!
@file storage.py
@brief Сохранение и загрузка расходов из файла.

Расходы хранятся в JSON-файле в виде списка словарей.
"""

import json
import os

## Имя файла, в котором хранятся расходы.
FILE_NAME = "expenses.json"


def load_expenses():
    """!
    @brief Загружает расходы из файла.

    @return Список расходов. Если файла нет, возвращается пустой список.
    """
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)


def save_expenses(expenses):
    """!
    @brief Сохраняет расходы в файл.

    Файл перезаписывается целиком. Кириллица сохраняется как есть.

    @param expenses Список расходов для сохранения.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)
