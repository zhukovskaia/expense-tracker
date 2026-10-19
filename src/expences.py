"""Добавление и просмотр расходов."""

import storage

_expenses = storage.load_expenses()


def get_expenses():
    return _expenses


def show_expenses():
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        line = f"{i}. {exp.get('date', '—')} | {exp['category']} — {exp['amount']} руб."
        if exp.get("comment"):
            line += f" ({exp['comment']})"
        print(line)
    print("-------------------")


def add_expense(category, amount, date, comment=""):
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
        print(f"Удалён расход: {removed['category']} — {removed['amount']} руб. ({removed.get('date', '—')})")
        return True
    else:
        print("Ошибка: расхода с таким номером не существует.")
        return False