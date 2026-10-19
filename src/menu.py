import expences

def show_menu():
    print("\n=== Учёт расходов ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Статистика по категориям")
    print("4. Удалить расход")
    print("5. Фильтр по категории")  # <--- Новый пункт
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
            expences.show_statistics()
        elif choice == "4":
            expences.show_expenses()
            try:
                index = int(input("Введите номер расхода для удаления: "))
                expences.delete_expense(index)
            except ValueError:
                print("Ошибка: нужно ввести число.")
        elif choice == "5":  # <--- Обработка фильтра
            search_cat = input("Введите категорию для поиска: ").strip()
            expences.filter_expenses(search_cat)
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте ещё раз.")