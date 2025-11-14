
def task_1():
    gradus=int(input("Введите температуру кондиционера, когорую вы хотите ввести: "))
    if gradus <= 20:
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

def task_4():
    number = input("Введите любое число :")
    summa = sum(map(int,list(number)))
    if summa % 3 == 0 and (int(number)%10)%2 == 0:
        print("Число делиться на 3!")
    else:
        print("Не делиться на 3")

def task_5():
    problem_password = []
    password = input("ВВедите пароль: ")
    spec_simvols = ".,:;!_*-+()/#¤%&"

    has_upper = False
    has_lower = False
    has_number = False
    has_spec_simvols = False
    len_passsword = False

    if len(password) >= 8:
        len_passsword = True
    else:
        problem_password.append("8 символов в коде")

    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True 
        if i.isdigit():
            has_number = True
        if i in spec_simvols:
            has_spec_simvols = True
    if (len_passsword and has_lower and has_number and has_spec_simvols and has_upper) == True:
        print("Пароль надежный! Он подходит")
    
    else:
        if not has_lower:
            problem_password.append("строчных букв")
        if not has_number:
            problem_password.append("цифр")
        if not has_spec_simvols:
            problem_password.append("спец символов")
        if not has_upper:
            problem_password.append("отсутствуют заглавные")
        print(f"У вас отсутствуют: {", ".join(problem_password)}") 
 
def task_6():
    try:
        year = int(input("Введите год для проверки на его високосность: "))
     
        if ((year % 4 == 0) and (year % 100 !=0)) or year % 400 == 0:
            print(f"{year} - Год високосный")
        else:
            print(f"{year} - Год не високосный")
    except:
        print("Введи цифры, а не чепуху")

def task_7():
    number = int(input("Введите три числа: "))
    if len(str(number)) == 3:
        b = list(str(number))
        if int(b[0])>=int(b[1])<=int(b[2]):
            print(int(b[1]))
        elif int(b[1])>=int(b[0])<=int(b[2]):
            print(int(b[0]))
        elif int(b[1])>=int(b[2])<=int(b[0]):
            print(int(b[2]))
        
    else:
        print("Введено не требовательное количество цифр")

def task_8():
    sum = int(input(("Введите сумму товара: ")))
    if sum < 1000:
        print("Ваша скидка: 0%")
        print(sum - ((sum/100)*0))
    if 1000 <= sum < 5000:
        print("Ваша скидка: 5%")
        print(sum - ((sum/100)*5))
    if 5000 <= sum < 10000:
        print("Ваша скидка: 10%")
        print(sum - ((sum/100)*10))
    if sum >= 10000:
        print("Ваша скидка: 15%")
        print(sum - ((sum/100)*15))
    
def task_9():
    sum = int(input(("Введите сумму товара: ")))
    if sum <= 5:
        print("Ночь")
    elif 6 <= sum <= 11:
        print("Утро")
    elif 12 <= sum <= 17:
        print("День")
    elif 18<= sum <= 23:
        print("Вечер")
    else:
        print("Введено больше 23 часов ")


def task_10():
    a = 0
    chislo = int(input("Введите число: "))
    for i in range(2, 9 + 1):
        if chislo % i != 0:
            a += 1
    if a == 8:
        print(f"{chislo} - простое число")
    else:
        print(f"{chislo} - составное число")

