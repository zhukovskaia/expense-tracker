"""!
@file menu.py
@brief Консольное меню программы.
"""

import expences
import stats
import validators


def show_menu():
    """!
    @brief Выводит пункты меню.
    """
    print("\n=== Учёт расходов ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Статистика по категориям")
    print("4. Удалить расход")
    print("5. Фильтр по категории")
    print("0. Выход")


def input_expense():
    """!
    @brief Запрашивает данные расхода и добавляет его.

    Категория, сумма и дата проверяются функциями из validators.py.
    """
    category = validators.read_category()
    amount = validators.read_amount()
    expense_date = validators.read_date()
    comment = input("Комментарий (необязательно): ").strip()
    expences.add_expense(category, amount, expense_date, comment)


def input_delete():
    """!
    @brief Показывает список расходов и удаляет расход по введённому номеру.
    """
    if not expences.get_expenses():
        print("Список расходов пуст.")
        return
    expences.show_expenses()
    try:
        index = int(input("Введите номер расхода для удаления: "))
    except ValueError:
        print("Ошибка: нужно ввести число.")
        return
    expences.delete_expense(index)


def run():
    """!
    @brief Главный цикл программы.

    Показывает меню и выполняет выбранный пункт, пока пользователь не выберет 0.
    """
    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            input_expense()
        elif choice == "2":
            expences.show_expenses()
        elif choice == "3":
            stats.show_statistics(expences.get_expenses())
        elif choice == "4":
            input_delete()
        elif choice == "5":
            search_cat = input("Введите категорию для поиска: ").strip()
            expences.filter_expenses(search_cat)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте ещё раз.")
