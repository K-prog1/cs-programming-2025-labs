
def task_1():
    gradus=int(input("Введите температуру кондиционера, когорую вы хотите ввести: "))
    if gradus < 20:
        print("Кондиционер включен")
    if gradus > 20:
        print("Кондиционер выключен")

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

def task_3():
    try:
        sobak = int(input("Введите собачьи года"))
    except ValueError:
        print("Введено не число")
        return 
    
    human = 10.5
    if 0 < sobak < 23:
        if sobak == 1:
            print("10,5")
        if sobak > 1:
            while sobak != 1:
                sobak -= 1
                human += 4.0
        print(human - 4.0)
    if sobak < 0: 
        print("эммм... собака не рождена")
    if sobak > 22:
        print("Возраст собаки не может превышать 22")

task_3()

def task_4():
    number = input("Введите любое число :")
    summa = sum(map(int,list(number)))
    if summa % 3 == 0 and (int(number)%10)%2 == 0:
        print("Число делиться на 3!")
    else:
        print("Не делиться на 3")

def task_5():
    a = 0
