"""Добавление, просмотр, удаление и фильтрация расходов."""

import storage

# Загружаем расходы из файла при старте
_expenses = storage.load_expenses()


def get_expenses():
    return _expenses


def _format_expense(i, exp):
    """Формирует строку для вывода одного расхода."""
    line = f"{i}. {exp.get('date', '—')} | {exp['category']} — {exp['amount']} руб."
    if exp.get("comment"):
        line += f" ({exp['comment']})"
    return line


def show_expenses():
    """Показать все расходы."""
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        print(_format_expense(i, exp))
    print("-------------------")


def add_expense(category, amount, date, comment=""):
    """Добавить расход и сохранить в файл."""
    _expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment,
    })
    storage.save_expenses(_expenses)
    print("Расход добавлен.")


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

    search = search_category.strip().lower()
    filtered = [exp for exp in _expenses if str(exp["category"]).strip().lower() == search]

    if not filtered:
        print(f"Расходов в категории '{search_category}' не найдено.")
        return

    print(f"\n--- Расходы по категории '{search_category}' ---")
    for i, exp in enumerate(filtered, start=1):
        print(_format_expense(i, exp))
    print("-------------------------------------------------")
