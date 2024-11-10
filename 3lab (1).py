import os
import tabulate  # библиотека для таблиц

# Столбцы данных (включая новый столбец "Тип кузова")
columns = ['№', 'Производитель', 'Марка', 'Цвет', 'Коробка передач', 'Привод']


# Функции ↓ ↓ ↓ ↓ ↓ ↓

def showdata():  # считывание данных из файла и их преобразование в таблицу
    with open("data_source.txt", 'r', encoding='utf-16') as file:
        lines = file.readlines()
    return [line.strip().split("/") for line in lines]


def find_num():  # нахождение последнего номера
    data = showdata()
    return max(int(car[0]) for car in data) if data else 0


def add_car_error():  # Страница 2. Добавить машину
    os.system('cls')
    print("_______________________")

    vvod_fabric = input("Введите производителя авто: ")
    if '/' in vvod_fabric: return add_car_error()

    vvod_model = input("Введите марку авто: ")
    if '/' in vvod_model: return add_car_error()

    vvod_color = input("Введите цвет авто: ")
    if '/' in vvod_color: return add_car_error()

    vvod_transmission = input("Введите коробку передач: ")
    if '/' in vvod_transmission: return add_car_error()

    vvod_engine = input("Введите привод авто: ")
    if '/' in vvod_engine: return add_car_error()



    num = find_num() + 1
    car_string = f'{num}/{vvod_fabric}/{vvod_model}/{vvod_color}/{vvod_transmission}/{vvod_engine}'

    # Считывание данных, добавление нового автомобиля и запись обратно в файл
    data = showdata()
    data.append([car_string])

    with open("data_source.txt", 'w', encoding='utf-16') as file:
        for car in data:
            file.write("/".join(car) + "\n")

    page_main()


def delete_car_func(car_num):  # Удалить машину
    os.system('cls')
    data = showdata()
    data = [car for car in data if int(car[0]) != car_num]

    # Обновление номеров
    for i, car in enumerate(data):
        car[0] = str(i + 1)

    with open("data_source.txt", 'w', encoding='utf-16') as file:
        for car in data:
            file.write("/".join(car) + "\n")

    page_main()


def change_car_func(car_num):  # Редактировать машину
    os.system('cls')
    data = showdata()

    car_to_edit = None
    for car in data:
        if int(car[0]) == car_num:
            car_to_edit = car
            break

    if not car_to_edit:
        print(f"Машина с номером {car_num} не найдена.")
        page_main()
        return

    print(tabulate.tabulate([car_to_edit], headers=columns, tablefmt='pipe'))

    print("1. Вернуться на главную")
    print("2. Заменить производителя")
    print("3. Заменить марку")
    print("4. Заменить цвет")
    print("5. Заменить коробку передач")
    print("6. Заменить привод")

    action = int(input("Выберите действие (1-6): "))

    if action == 1:
        page_main()
    else:
        new_value = input(f"Введите новое значение для {columns[action - 1]}: ")
        if '/' in new_value: return change_car_func(car_num)

        car_to_edit[action - 1] = new_value

        # Записываем обновленные данные в файл
        with open("data_source.txt", 'w', encoding='utf-16') as file:
            for car in data:
                file.write("/".join(car) + "\n")

        page_main()


def find_car():  # Страница 5. Найти машину
    os.system('cls')
    data = showdata()

    print("Выберите критерий поиска:")
    print("1. По номеру")
    print("2. По цвету")
    print("3. По коробке передач")
    print("4. По приводу")

    search_criteria = int(input("Введите номер критерия (1-4): "))
    search_value = input("Введите значение для поиска: ").strip()

    results = [car for car in data if (search_criteria == 1 and search_value == car[0]) or
               (search_criteria == 2 and search_value.lower() == car[3].lower()) or
               (search_criteria == 3 and search_value.lower() == car[4].lower()) or
               (search_criteria == 4 and search_value.lower() == car[5].lower())]

    if results:
        print("Найденные автомобили:")
        print(tabulate.tabulate(results, headers=columns, tablefmt='pipe'))
    else:
        print("Автомобили не найдены по вашему запросу.")

    print("\n1. Вернуться на главную")
    print("2. Повторить поиск")
    action = int(input("Для выбора действия введите его номер (1-2): "))

    if action == 1:
        page_main()
    elif action == 2:
        find_car()


def page_main():
    os.system('cls')
    print("Главное меню:")
    print("1. Показать все автомобили")
    print("2. Добавить автомобиль")
    print("3. Редактировать автомобиль")
    print("4. Удалить автомобиль")
    print("5. Найти автомобиль")
    print("6. Выход")

    choice = int(input("Выберите действие (1-6): "))
    if choice == 1:
        show_all_cars()
    elif choice == 2:
        add_car_error()
    elif choice == 3:
        edit_car_page()
    elif choice == 4:
        delete_car_page()
    elif choice == 5:
        find_car()
    elif choice == 6:
        exit_program()
    else:
        print("Неверный выбор. Попробуйте снова.")
        page_main()


def show_all_cars():
    os.system('cls')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))

    print("\n1. Вернуться на главную")
    print("2. Повторить просмотр")
    action = int(input("Для выбора действия введите его номер (1-2): "))
    if action == 1:
        page_main()
    elif action == 2:
        show_all_cars()


def edit_car_page():
    os.system('cls')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))

    try:
        car_num = int(input("Введите номер автомобиля для редактирования: "))
        change_car_func(car_num)
    except ValueError:
        print("Неверный ввод. Попробуйте снова.")
        edit_car_page()


def delete_car_page():
    os.system('cls')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))

    try:
        car_num = int(input("Введите номер автомобиля для удаления: "))
        delete_car_func(car_num)
    except ValueError:
        print("Неверный ввод. Попробуйте снова.")
        delete_car_page()


def exit_program():
    print("Выход из программы...")
    exit()


# Стартовая страница
page_main()
