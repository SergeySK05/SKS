import os
import tabulate  #библиотека для таблиц

columns = ['№', 'Производитель', 'Марка', 'Цвет', 'Коробка передач', 'Привод'] #названия столбцов

#Функции ↓ ↓ ↓ ↓ ↓ ↓
def showdata(): #txt в таблицу
    d=open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16').readlines()
    r=[]
    for i in d:
        s=[x for x in i.split("/")]
        r.append(s)
    return r
def find_num(): #нахождение последнего номера
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt',encoding='utf-16').readlines()
    r=[]
    number=0
    for i in d:
        s = [x for x in i.split("/")]
        r.append(s)
    for i in range(len(r)):
        num1=r[i][0]
        if int(num1)>number:
            number=int(num1)
    return number
def delete_car_func(x): # Удалить машину функция
    os.system('cls')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))  # таблица
    print("")
    number_for_delete = x
    os.system('cls')
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16').readlines()
    file = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16')
    rdata = []
    for i in d:
        s = [x for x in i.split("/")]
        if int(s[0]) != number_for_delete: #убираем машину
            rdata.append(s)
    for i in range(len(rdata)): #сдвигаем номер
        rdata[i][0]=str(i+1)
    s = ["/".join(x) for x in rdata]
    file.truncate(0)
    for i in s: #редачим файл
        file.write(str(i))
    file.close()
    page_data()
def change_car_func(x): #Редачить машину функция
    os.system('cls')
    data=showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe')) #таблица
    print("")
    number_for_change = x
    os.system('cls')
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16').readlines()
    rdata=[]
    for i in d:
        r = []
        s = [x for x in i.split("/")]
        rdata.append(s)
        if int(s[0]) == number_for_change: #сравниваем номер
            r.append(s)
            print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
    print("")
    print("1.Вернуться на главную")
    print("2.Заменить производителя")
    print("3.Заменить марку")
    print("4.Заменить цвет")
    print("5.Заменить коробку передач")
    print("6.Заменить привод")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            vvod_data = int(input("Для выбора действия введите его номер(1-6):"))
            k+=1
        except: print("")
    if vvod_data==1:
        os.system('cls')
        page_main()
    else:
        os.system('cls')
        r2 = []
        for i in d:
            s = [x for x in i.split("/")]
            if int(s[0]) == number_for_change:
                r2.append(s)
                print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
        print("")
        print(f"Заменить {columns[vvod_data-1]}")
        rdata[number_for_change - 1][vvod_data-1] = r2[0][vvod_data-1] = input(f'{r2[0][vvod_data-1]} => ')
        os.system('cls')
        print(tabulate.tabulate(r2, headers=columns, tablefmt='pipe'))
        file = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16')
        s = ["/".join(x) for x in rdata]
        for i in s: #редачим файл
            file.write(str(i))
        file.close()
        print("1.Вернуться на главную")
        print("2.Повторная замена")
        k=0
        while k==0: #проверка на буквы
            try:
                vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except:
                print("")
        if vvod_data3 == 1:
            os.system('cls')
            page_main()
        elif vvod_data3 == 2:
            change_car()
def add_car_error(): #Page 2. Добавить машину
    os.system('cls')
    data = showdata()
    d2 = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16').readlines()
    file = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16')
    print("Введен запрещенный символ => / ")
    print("_______________________")
    vvod_fabric = input("Введите производителя авто:")
    if vvod_fabric.count("/")==0:
        vvod_model = input("Введите марку авто:")
        if vvod_model.count("/")==0:
            vvod_color = input("Введите цвет авто:")
            if vvod_color.count("/")==0:
                vvod_transmission = input("Введите коробку передач:")
                if vvod_transmission.count("/")==0:
                    vvod_engine = input("Введите привод авто:")
                    num=find_num()+1
                    car_string = f'{num}/{vvod_fabric}/{vvod_model}/{vvod_color}/{vvod_transmission}/{vvod_engine}' #новая строка
                    for i in d2:
                        file.write(str(i))
                    file.write(f"{car_string}\n")
                    file.close()
                    page_data()
                else:
                    add_car_error()
            else:
                add_car_error()
        else:
            add_car_error()
    else:
        add_car_error()

#Страницы ↓ ↓ ↓ ↓ ↓ ↓
def page_main():  # основная страница
    print('База данных машин')
    print('1.Список машин')
    print('2.Добавить авто')
    print('3.Удалить авто')
    print('4.Изменить авто')
    print('5.Поиск авто')
    print('')
    k=0
    while k==0: #проверка на буквы
        try:
            vvod_main = int(input("Для выбора страницы введите ее номер(1-5):"))
            k+=1
        except:
            print("")
    if vvod_main == 1:
        page_data()
    elif vvod_main == 2:
        add_car()
    elif vvod_main == 3:
        delete_car()
    elif vvod_main == 4:
        change_car()
    elif vvod_main == 5:
        find_car()
    else:
        os.system('cls')
        page_main()
def page_data():  # Page 1.Список машин
    os.system('cls')
    print("Список машин")
    data=showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))
    print("")
    print("_______________________")
    print("1.Вернуться на главную")
    print("2.Добавить авто")
    print("3.Удалить авто")
    print('4.Изменить авто')
    k=0
    while k==0: #проверка на буквы
        try:
            vvod_data = int(input("Для выбора действия введите его номер(1-4):"))
            k+=1
        except: print("")
    if vvod_data==1:
        os.system('cls')
        page_main()
    elif vvod_data==2:
        add_car()
    elif vvod_data==3:
        delete_car()
    elif vvod_data==4:
        change_car()
    else:
        os.system('cls')
        page_data()
def add_car(): #Page 2. Добавить машину
    os.system('cls')
    data = showdata()
    d2 = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16').readlines()
    file = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+',encoding='utf-16')
    vvod_fabric = input("Введите производителя авто:")
    if vvod_fabric.count("/") == 0:
        vvod_model = input("Введите марку авто:")
        if vvod_model.count("/") == 0:
            vvod_color = input("Введите цвет авто:")
            if vvod_color.count("/") == 0:
                vvod_transmission = input("Введите коробку передач:")
                if vvod_transmission.count("/") == 0:
                    vvod_engine = input("Введите привод авто:")
                    num = find_num() + 1
                    car_string = f'{num}/{vvod_fabric}/{vvod_model}/{vvod_color}/{vvod_transmission}/{vvod_engine}'  # новая строка
                    for i in d2:
                        file.write(str(i))
                    file.write(f"{car_string}\n")
                    file.close()
                    page_data()
                else:
                    add_car_error()
            else:
                add_car_error()
        else:
            add_car_error()
    else:
        add_car_error()
def delete_car(): #Page 3. Удалить машину
    os.system('cls')
    data = showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe'))  # таблица
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16').readlines()
    lines = len(d)
    print("")
    print("_______________________")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            number_for_delete = int(input(f"Для удаления машины введите ее номер | Всего машин - {lines} : "))
            k+=1
        except: print("")
    if number_for_delete<=lines:
        os.system('cls')
        file = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16')
        rdata = []
        for i in d:
            s = [x for x in i.split("/")]
            if int(s[0]) != number_for_delete: #убираем машину
                rdata.append(s)
        for i in range(len(rdata)): #сдвигаем номер
            rdata[i][0]=str(i+1)
        s = ["/".join(x) for x in rdata]
        file.truncate(0)
        for i in s: #редачим файл
            file.write(str(i))
        file.close()
        page_data()
    else:
        os.system('cls')
        print("Машины с таким номером нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Удалить авто")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except: print("")
        if vvod_data == 1:
            os.system('cls')
            page_main()
        elif vvod_data == 2:
            delete_car()
def change_car(): #Page 4. Редачить машину
    os.system('cls')
    data=showdata()
    print(tabulate.tabulate(data, headers=columns, tablefmt='pipe')) #таблица
    print("")
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16').readlines()
    lines=len(d)
    print("_______________________")
    k = 0
    while k == 0:  # проверка на буквы
        try:
            number_for_change = int(input(f"Для редактирования данных машины введите ее номер | Всего машин - {lines} : "))
            k+=1
        except: print("")
    if number_for_change<=lines:
        os.system('cls')
        rdata=[]
        for i in d:
            r = []
            s = [x for x in i.split("/")]
            rdata.append(s)
            if int(s[0]) == number_for_change: #сравниваем номер
                r.append(s)
                print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
        print("")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Изменить производителя")
        print("3.Изменить марку")
        print("4.Изменить цвет")
        print("5.Изменить коробку передач")
        print("6.Изменить привод")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-6):"))
                k+=1
            except: print("")
        if vvod_data==1:
            os.system('cls')
            page_main()
        elif vvod_data<=6:
            os.system('cls')
            r2 = []
            for i in d:
                s = [x for x in i.split("/")]
                if int(s[0]) == number_for_change:
                    r2.append(s)
                    print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
            print("")
            print(f"Заменить {columns[vvod_data-1]}")
            rdata[number_for_change - 1][vvod_data-1] = r2[0][vvod_data-1] = input(f'{r2[0][vvod_data-1]} => ')
            os.system('cls')
            print(tabulate.tabulate(r2, headers=columns, tablefmt='pipe'))
            file = open('data_source.txt', 'r+',encoding='utf-16')
            s = ["/".join(x) for x in rdata]
            for i in s: #редачим файл
                file.write(str(i))
            file.close()
            print("_______________________")
            print("1.Вернуться на главную")
            print("2.Повторная замена")
            k = 0
            while k == 0:  # проверка на буквы
                try:
                    vvod_data3 = int(input("Для выбора действия введите его номер(1-2):"))
                    k+=1
                except: print("")
            if vvod_data3 == 1:
                os.system('cls')
                page_main()
            elif vvod_data3 == 2:
                change_car()
            else:
                os.system('cls')
                page_main()
        else:
            os.system('cls')
            change_car()
    else:
        os.system('cls')
        print("Машины с таким номером нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Изменить авто")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except: print("")
        if vvod_data == 1:
            os.system('cls')
            page_main()
        elif vvod_data == 2:
            change_car()
        else:
            os.system('cls')
            page_main()
'''
def find_car(): #Page 5. Найти машину
    os.system('cls')
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16').readlines()
    lines = len(d)
    k = 0
    while k == 0:  # проверка на буквы
        try:
            number_for_find=int(input(f"Для поиска машины введите ее номер | Всего машин - {lines} : "))
            k+=1
        except: print("")
    if number_for_find<=lines:
        for i in d:
            r=[]
            s = [x for x in i.split("/")]
            if int(s[0])==number_for_find:
                r.append(s)
                print(tabulate.tabulate(r, headers=columns, tablefmt='pipe'))
        print("")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Повторный поиск")
        print("3.Удалить эту машину")
        print("4.Изменить эту машину")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-4):"))
                k+=1
            except: print("")
        if vvod_data == 1:
            os.system('cls')
            page_main()
        elif vvod_data == 2:
            find_car()
        elif vvod_data == 3:
            delete_car_func(number_for_find)
        elif vvod_data == 4:
            change_car_func(number_for_find)
    else:
        os.system('cls')
        print("Машины с таким номером нет")
        print("_______________________")
        print("1.Вернуться на главную")
        print("2.Повторный поиск")
        k = 0
        while k == 0:  # проверка на буквы
            try:
                vvod_data = int(input("Для выбора действия введите его номер(1-2):"))
                k+=1
            except:
                print("")
        if vvod_data == 1:
            os.system('cls')
            page_main()
        elif vvod_data == 2:
            find_car()
        else:
            os.system('cls')
            page_main()
'''


def find_car():  # Page 5. Найти машину
    os.system('cls')
    d = open('C:/Users/Глеб/Desktop/новая/data_source.txt', 'r+', encoding='utf-16').readlines()

    print("Выберите критерий поиска:")
    print("1. По номеру")
    print("2. По цвету")
    print("3. По коробке передач")
    print("4. По приводу")

    search_criteria = None
    while search_criteria not in {1, 2, 3, 4}:
        try:
            search_criteria = int(input("Введите номер критерия (1-4): "))
            if search_criteria not in {1, 2, 3, 4}:
                print("Пожалуйста, выберите номер от 1 до 4.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    search_value = input("Введите значение для поиска: ").strip()
    if not search_value:
        print("Значение для поиска не может быть пустым.")
        return

    results = []
    for i in d:
        s = [x for x in i.split("/")]
        print(f"Проверяем: Привод: {s[5]}, Искомое значение: {search_value}")  # Отладочный вывод
        if (search_criteria == 1 and search_value == s[0]) or \
                (search_criteria == 2 and search_value.lower() == s[3].lower()) or \
                (search_criteria == 3 and search_value.lower() == s[4].lower()) or \
                (search_criteria == 4 and search_value.lower() == s[5].strip().lower()):
            results.append(s)

    if results:
        print(tabulate.tabulate(results, headers=columns, tablefmt='pipe'))
    else:
        print("Машины с такими данными не найдены.")

    print("_______________________")
    print("1. Вернуться на главную")
    print("2. Повторный поиск")
    while True:
        try:
            vvod_data = int(input("Для выбора действия введите его номер (1-2): "))
            if vvod_data in {1, 2}:
                break
            else:
                print("Пожалуйста, выберите номер 1 или 2.")
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")

    if vvod_data == 1:
        os.system('cls')
        page_main()
    elif vvod_data == 2:
        find_car()



page_main()
