"""Добавление и просмотр расходов."""

import storage

# Загружаем расходы из файла при старте
_expenses = storage.load_expenses()


def show_expenses():
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        print(f"{i}. {exp['category']} — {exp['amount']} руб. ({exp['comment']})")
    print("-------------------")


def add_expense(category, amount, comment=""):
    _expenses.append({"category": category, "amount": amount, "comment": comment})
    storage.save_expenses(_expenses)
    print("Расход добавлен.")