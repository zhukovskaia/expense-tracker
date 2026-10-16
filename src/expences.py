"""Добавление и просмотр расходов."""

_expenses = [
    {"category": "Еда", "amount": 450, "comment": "Обед"},
    {"category": "Транспорт", "amount": 60, "comment": "Метро"},
]


def show_expenses():
    if not _expenses:
        print("Список расходов пуст.")
        return
    print("\n--- Все расходы ---")
    for i, exp in enumerate(_expenses, start=1):
        print(f"{i}. {exp['category']} — {exp['amount']} руб. ({exp['comment']})")
    print("-------------------")