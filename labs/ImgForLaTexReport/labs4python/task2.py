def task_2():
    month = int(input("Введите номер месяца: "))
    if 0< month < 13: 
        if 3 <= month <= 5:
            print("Весна")
        if 6 <= month <= 8:
            print("Лето")
        if 9 <= month <= 11:
            print("Осень")
        if  month == 12 or month <= 2:
            print("Зима")
    else:
        print('номерация месяца не может быть отрицательным или больше 12')
