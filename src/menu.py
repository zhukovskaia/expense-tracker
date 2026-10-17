import expences


def show_menu():
    print("\n=== Учёт расходов ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Статистика по категориям")
    print("0. Выход")


def run():
    while True:
        show_menu()
        choice = input("Выберите пункт: ").strip()
        if choice == "1":
            category = input("Категория: ").strip()
            amount = input("Сумма: ").strip()
            comment = input("Комментарий (необязательно): ").strip()
            expences.add_expense(category, amount, comment)
        elif choice == "2":
            expences.show_expenses()
        elif choice == "3":
            print("Статистика (скоро)")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте ещё раз.")