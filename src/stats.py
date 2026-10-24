"""
@file stats.py
@brief Модуль для подсчёта статистики по расходам.

Содержит функции подсчёта общей суммы и разбивки по категориям,
а также функцию вывода статистики в консоль.
"""


def _amount(exp):
    """
    @brief Вспомогательная функция: получить сумму расхода как float.

    @param exp Словарь с полем 'amount'.
    @return Сумма как float или None, если значение некорректно.

    @note Внутренняя функция (начинается с подчёркивания).
    """
    try:
        return float(exp["amount"])
    except (KeyError, TypeError, ValueError):
        return None


def total_amount(expenses):
    """
    @brief Считает общую сумму всех расходов.

    @param expenses Список словарей с расходами.
    @return Общая сумма как float. Некорректные записи игнорируются.
    """
    total = 0.0
    for exp in expenses:
        amount = _amount(exp)
        if amount is not None:
            total += amount
    return total


def stats_by_category(expenses):
    """
    @brief Считает сумму по каждой категории.

    @param expenses Список словарей с расходами.
    @return Словарь {категория: сумма}, отсортированный по убыванию суммы.

    @note Категория приводится к нижнему регистру; пустая категория заменяется на "без категории".
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
    """
    @brief Выводит общую сумму и статистику по категориям в консоль.

    @param expenses Список словарей с расходами.

    @note Помимо суммы в рублях показывает процент каждой категории от общей суммы.
    """
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