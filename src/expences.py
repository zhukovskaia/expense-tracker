"""Добавление и просмотр расходов."""

import storage

_expenses = storage.load_expenses()


def show_expenses():
    """Показать все расходы."""
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        print(f"{i}. {exp['category']} — {exp['amount']} руб. ({exp['comment']})")
    print("-------------------")


def add_expense(category, amount, comment=""):
    """Добавить расход и сохранить в файл."""
    _expenses.append({"category": category, "amount": amount, "comment": comment})
    storage.save_expenses(_expenses)
    print("Расход добавлен.")


def show_statistics():
    """Показать статистику по категориям."""
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
    """Удалить расход по его номеру."""
    if 0 < index <= len(_expenses):
        removed = _expenses.pop(index - 1)
        storage.save_expenses(_expenses)
        print(f"Удалён расход: {removed['category']} — {removed['amount']} руб.")
    else:
        print("Расхода с таким номером не существует.")


def filter_expenses(search_category):
    """Показать расходы только по выбранной категории."""
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