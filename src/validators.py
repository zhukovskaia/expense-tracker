"""!
@file validators.py
@brief Проверка пользовательского ввода.

Каждая функция переспрашивает пользователя, пока ввод не станет корректным.
"""

import math
from datetime import datetime

## Формат даты расхода: ГГГГ-ММ-ДД.
DATE_FORMAT = "%Y-%m-%d"


def read_amount(prompt="Сумма: "):
    """!
    @brief Запрашивает сумму, пока не будет введено положительное число.

    Запятая принимается как десятичный разделитель (99,90 = 99.90).

    @param prompt Текст приглашения к вводу.
    @return Сумма как число с плавающей точкой (больше нуля).
    """
    while True:
        text = input(prompt).strip().replace(",", ".")
        try:
            amount = float(text)
        except ValueError:
            print("Ошибка: введите число, например 350 или 99.90.")
            continue
        if not math.isfinite(amount):
            print("Ошибка: введите обычное число.")
            continue
        if amount <= 0:
            print("Ошибка: сумма должна быть больше нуля.")
            continue
        return amount


def read_date(prompt="Дата (ГГГГ-ММ-ДД, Enter - сегодня): "):
    """!
    @brief Запрашивает дату в формате ГГГГ-ММ-ДД.

    @param prompt Текст приглашения к вводу.
    @return Дата строкой в формате ГГГГ-ММ-ДД.
            Если пользователь нажал Enter, возвращается сегодняшняя дата.
    """
    while True:
        text = input(prompt).strip()
        if not text:
            return datetime.now().strftime(DATE_FORMAT)
        try:
            datetime.strptime(text, DATE_FORMAT)
        except ValueError:
            print("Ошибка: неверная дата. Пример: 2026-10-16.")
            continue
        return text


def read_category(prompt="Категория: "):
    """!
    @brief Запрашивает категорию, пока она не будет непустой.

    @param prompt Текст приглашения к вводу.
    @return Категория в нижнем регистре без пробелов по краям.
    """
    while True:
        text = input(prompt).strip().lower()
        if text:
            return text
        print("Ошибка: категория не может быть пустой.")
