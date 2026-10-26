from datetime import datetime

import stats
import storage

_expenses = storage.load_expenses()


def get_expenses():
    return _expenses


def add_expense(category, amount, date=None, comment=""):
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    _expenses.append({
        "date": date,
        "category": category,
        "amount": amount,
        "comment": comment,
    })
    storage.save_expenses(_expenses)
    print("Расход добавлен.")


def _format(number, exp):
    line = f"{number}. {exp.get('date', '')} | {exp.get('category', '')} — {exp.get('amount', 0)} руб."
    comment = exp.get("comment", "")
    if comment:
        line += f" ({comment})"
    return line


def show_expenses():
    if not _expenses:
        print("Список расходов пуст.")
        return
    for number, exp in enumerate(_expenses, start=1):
        print(_format(number, exp))


def show_statistics():
    stats.show_statistics(_expenses)


def delete_expense(index):
    if index < 1 or index > len(_expenses):
        print("Ошибка: расхода с таким номером нет.")
        return
    _expenses.pop(index - 1)
    storage.save_expenses(_expenses)
    print("Расход удалён.")


def filter_expenses(category):
    category = category.strip().lower()
    found = [
        (number, exp)
        for number, exp in enumerate(_expenses, start=1)
        if str(exp.get("category", "")).strip().lower() == category
    ]
    if not found:
        print("Расходов в этой категории нет.")
        return
    for number, exp in found:
        print(_format(number, exp))
    total = stats.total_amount([exp for _, exp in found])
    print(f"Итого по категории: {total:.2f} руб.")