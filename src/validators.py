
import math
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


def read_amount(prompt="Сумма: "):
    """Запрашивает сумму, пока не будет введено положительное число.

    Возвращает сумму как число с плавающей точкой.
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
    """Запрашивает дату в формате ГГГГ-ММ-ДД.

    Если пользователь нажал Enter, возвращает сегодняшнюю дату.
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
    """Запрашивает категорию, пока она не будет непустой."""
    while True:
        text = input(prompt).strip().lower()
        if text:
            return text
        print("Ошибка: категория не может быть пустой.")