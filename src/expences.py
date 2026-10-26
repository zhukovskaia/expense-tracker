"""!
@file expences.py
@brief Добавление, просмотр, удаление и фильтрация расходов.

Расход — словарь с ключами:
- date — дата в формате ГГГГ-ММ-ДД;
- category — категория;
- amount — сумма;
- comment — комментарий (может быть пустым).
"""

import storage

## Список расходов. Загружается из файла при старте программы.
_expenses = storage.load_expenses()


def get_expenses():
    """!
    @brief Возвращает список всех расходов.

    @return Список расходов.
    """
    return _expenses


def _format_expense(i, exp):
    """!
    @brief Формирует строку для вывода одного расхода.

    @param i Номер расхода в списке.
    @param exp Расход.
    @return Строка вида "1. 2026-10-16 | еда — 350.0 руб. (обед)".
    """
    line = f"{i}. {exp.get('date', '—')} | {exp['category']} — {exp['amount']} руб."
    if exp.get("comment"):
        line += f" ({exp['comment']})"
    return line


def show_expenses():
    """!
    @brief Выводит все расходы с номерами.
    """
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        print(_format_expense(i, exp))
    print("-------------------")


def add_expense(category, amount, date, comment=""):
    """!
    @brief Добавляет расход и сохраняет его в файл.

    @param category Категория.
    @param amount Сумма.
    @param date Дата в формате ГГГГ-ММ-ДД.
    @param comment Комментарий (необязательно).
    """
    _expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment,
    })
    storage.save_expenses(_expenses)
    print("Расход добавлен.")


def delete_expense(index):
    """!
    @brief Удаляет расход по его номеру и сохраняет изменения в файл.

    @param index Номер расхода в списке (начиная с 1).
    """
    if 0 < index <= len(_expenses):
        removed = _expenses.pop(index - 1)
        storage.save_expenses(_expenses)
        print(f"Удалён расход: {removed['category']} — {removed['amount']} руб.")
    else:
        print("Расхода с таким номером не существует.")


def filter_expenses(search_category):
    """!
    @brief Выводит расходы только по выбранной категории.

    Категории сравниваются без учёта регистра и пробелов по краям.

    @param search_category Категория для поиска.
    """
    if not _expenses:
        print("Список расходов пуст.")
        return

    search = search_category.strip().lower()
    filtered = [exp for exp in _expenses if str(exp["category"]).strip().lower() == search]

    if not filtered:
        print(f"Расходов в категории '{search_category}' не найдено.")
        return

    print(f"\n--- Расходы по категории '{search_category}' ---")
    for i, exp in enumerate(filtered, start=1):
        print(_format_expense(i, exp))
    print("-------------------------------------------------")
