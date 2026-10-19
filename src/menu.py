from datetime import date, datetime

import expences

DATE_FORMAT = "%d.%m.%Y"


def show_menu():
    print("\n=== Учёт расходов ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Статистика по категориям")
    print("0. Выход")


def input_amount():
    while True:
        text = input("Сумма: ").strip().replace(",", ".")
        try:
            amount = float(text)
        except ValueError:
            print("Сумма должна быть числом.")
            continue
        if amount <= 0:
            print("Сумма должна быть больше нуля.")
            continue
        return amount


def input_date():
    today = date.today().strftime(DATE_FORMAT)
    while True:
        text = input(f"Дата (ДД.ММ.ГГГГ, Enter — {today}): ").strip()
        if not text:
            return today
        try:
            return datetime.strptime(text, DATE_FORMAT).strftime(DATE_FORMAT)
        except ValueError:
            print("Неверный формат даты.")


def input_expense():
    category = input("Категория: ").strip()
    while not category:
        print("Категория не может быть пустой.")
        category = input("Категория: ").strip()
    amount = input_amount()
    expense_date = input_date()
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
            print("Статистика (скоро)")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неверный пункт, попробуйте ещё раз.")
