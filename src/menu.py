import expences
import stats
import validators


def show_menu():
    print("\n=== Учёт расходов ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Статистика по категориям")
    print("4. Удалить расход")  # <--- Новый пункт
    print("0. Выход")


def input_expense():
    category = validators.read_category()
    amount = validators.read_amount()
    expense_date = validators.read_date()
    comment = input("Комментарий (необязательно): ").strip()
    expences.add_expense(category, amount, expense_date, comment)


def run():
    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            input_expense()
        elif choice == "2":
            expences.show_expenses()
        elif choice == "3":
            stats.show_statistics(expences.get_expenses())
        elif choice == "4":  # <--- Обработка удаления
            expences.show_expenses()
            try:
                index = int(input("Введите номер расхода для удаления: "))
                expences.delete_expense(index)
            except ValueError:
                print("Ошибка: нужно ввести целое число.")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте ещё раз.")