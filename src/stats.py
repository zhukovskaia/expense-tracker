"""Подсчёт общей суммы и статистики по категориям."""


def _amount(exp):
    """Возвращает сумму расхода числом или None, если сумма некорректна."""
    try:
        return float(exp["amount"])
    except (KeyError, TypeError, ValueError):
        return None


def total_amount(expenses):
    """Считает общую сумму всех расходов."""
    total = 0.0
    for exp in expenses:
        amount = _amount(exp)
        if amount is not None:
            total += amount
    return total


def stats_by_category(expenses):
    """Считает сумму по каждой категории.

    Возвращает словарь {категория: сумма}, отсортированный по убыванию суммы.
    """
    result = {}
    for exp in expenses:
        amount = _amount(exp)
        if amount is None:
            continue
        category = str(exp.get("category", "")).strip().lower() or "без категории"
        result[category] = result.get(category, 0.0) + amount
    return dict(sorted(result.items(), key=lambda item: item[1], reverse=True))


def show_statistics(expenses):
    """Выводит общую сумму и статистику по категориям."""
    if not expenses:
        print("Список расходов пуст.")
        return
    total = total_amount(expenses)
    print("\n--- Статистика по категориям ---")
    for category, amount in stats_by_category(expenses).items():
        percent = amount / total * 100 if total else 0
        print(f"{category}: {amount:.2f} руб. ({percent:.1f}%)")
    print("--------------------------------")
    print(f"Итого: {total:.2f} руб.")
