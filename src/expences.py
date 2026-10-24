"""
@file expences.py
@brief Модуль для работы с расходами: просмотр, добавление, удаление, фильтрация.

Содержит глобальный список _expenses, который загружается из файла при старте
и синхронизируется с ним при каждом изменении.
"""

import storage

_expenses = storage.load_expenses()


def show_expenses():
    """
    @brief Показать все расходы.

    Выводит в консоль нумерованный список всех расходов.
    Если список пуст — выводит предупреждение и завершает работу.
    """
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        print(f"{i}. {exp['category']} — {exp['amount']} руб. ({exp['comment']})")
    print("-------------------")


def add_expense(category, amount, comment=""):
    """
    @brief Добавить расход и сохранить в файл.

    @param category Строка — категория расхода (например, "Еда").
    @param amount   Сумма расхода (строка или число).
    @param comment  Необязательный комментарий (по умолчанию пустая строка).

    @note После добавления вызывает storage.save_expenses() для записи в файл.
    """
    _expenses.append({"category": category, "amount": amount, "comment": comment})
    storage.save_expenses(_expenses)
    print("Расход добавлен.")


def show_statistics():
    """
    @brief Показать статистику по категориям.

    Считает сумму расходов в каждой категории (суммы приводятся к float).
    Выводит список категорий и итоговую сумму.
    Некорректные суммы (которые нельзя преобразовать в float) пропускаются.
    """
    if not _expenses:
        print("Нет данных для статистики.")
        return
    stats = {}
    for exp in _expenses:
        category = exp["category"]
        try:
            amount = float(str(exp["amount"]).replace(",", "."))
        except ValueError:
            continue
        if category in stats:
            stats[category] += amount
        else:
            stats[category] = amount
    print("\n--- Статистика по категориям ---")
    total = 0
    for cat, amount in stats.items():
        print(f"{cat}: {amount} руб.")
        total += amount
    print(f"ИТОГО: {total} руб.")
    print("--------------------------------")


def delete_expense(index):
    """
    @brief Удалить расход по его номеру.

    @param index Порядковый номер расхода в списке (нумерация начинается с 1).

    @note Если номер вне диапазона — выводит сообщение об ошибке.
    @note После удаления вызывает storage.save_expenses() для синхронизации с файлом.
    """
    if 0 < index <= len(_expenses):
        removed = _expenses.pop(index - 1)
        storage.save_expenses(_expenses)
        print(f"Удалён расход: {removed['category']} — {removed['amount']} руб.")
    else:
        print("Расхода с таким номером не существует.")


def filter_expenses(search_category):
    """
    @brief Показать расходы только по выбранной категории.

    @param search_category Категория для поиска (регистр не важен).

    @note Если ничего не найдено — выводит соответствующее сообщение.
    """
    if not _expenses:
        print("Список расходов пуст.")
        return

    filtered = [exp for exp in _expenses if exp['category'].lower() == search_category.lower()]

    if not filtered:
        print(f"Расходов в категории '{search_category}' не найдено.")
        return

    print(f"\n--- Расходы по категории '{search_category}' ---")
    for i, exp in enumerate(filtered, start=1):
        print(f"{i}. {exp['amount']} руб. ({exp['comment']})")
    print("-------------------------------------------------")