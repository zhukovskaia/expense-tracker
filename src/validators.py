"""
@file validators.py
@brief Модуль валидации пользовательского ввода.

Содержит функции безопасного чтения суммы, даты и категории,
которые повторяют запрос при некорректном вводе.
"""

import math
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"
"""
@brief Формат даты, используемый в программе (ГГГГ-ММ-ДД).
"""


def read_amount(prompt="Сумма: "):
    """
    @brief Запрашивает сумму, пока не будет введено положительное число.

    @param prompt Приглашение к вводу (по умолчанию "Сумма: ").
    @return Сумма как число с плавающей точкой (float).

    @note Запятая автоматически заменяется на точку (для удобства пользователя).
    @note Отклоняет: нечисловые значения, бесконечность, NaN и числа <= 0.
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
    """
    @brief Запрашивает дату в формате ГГГГ-ММ-ДД.

    @param prompt Приглашение к вводу.
    @return Строка с датой в формате DATE_FORMAT.

    @note Если пользователь нажал Enter, возвращает сегодняшнюю дату.
    @note При неверном формате запрашивает дату повторно.
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
    """
    @brief Запрашивает категорию, пока она не будет непустой.

    @param prompt Приглашение к вводу.
    @return Непустая строка с названием категории (в нижнем регистре).

    @note Пустая строка не принимается.
    """
    while True:
        text = input(prompt).strip().lower()
        if text:
            return text
        print("Ошибка: категория не может быть пустой.")