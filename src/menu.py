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
            print("Добавление расхода (скоро)")
        elif choice == "2":
            print("Просмотр расходов (скоро)")
        elif choice == "3":
            print("Статистика (скоро)")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте ещё раз.")