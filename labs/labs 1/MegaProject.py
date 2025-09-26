text = "Danya"
number = 123123123
floatN = 67.3
a = True

def task2():
    print(text, number)

def task3():
    number_1 = 567
    number_2 = 23.4
    number_3 = "22"
    result = number_1 + number_2 + int(number_3)
    print(result)

def task4():
    a = 3
    b = 8
    c = (a + 4 * b) * (a - 3 * b) + a ** 2
    print(c)

def task5():
    a = int(input())
    b = int(input())
    result_p = a * 2 + b * 2
    result_S = a * b
    print(f"Периметр: {result_p}, Площадь: {result_S}.")

def task6():
    print("*   *   *")
    print(" * * * *")
    print("  *   *")

def task7():
    age_1 = 18
    age_2 = 21
    print(age_1 + age_2)
    print(age_1 - age_2)
    print(age_1 * age_2)
    print(age_1 // age_2)
    print(age_1 / age_2)
    print(age_1 % age_2)
    print(age_1 ** 2, age_2 ** 2)
    print(age_1 > age_2, age_1 < age_2, age_1 == age_2, age_1 >= age_2, age_1 <= age_2, age_1 != age_2)

def task8():
    a = "Slava"
    b = 52
    print(f"Меня зовут {a}, мой возраст{b}.")

def task9():
    text = "Сьешь еще и этих мягких французских булок, да выпей чаю."
    a = text.split(' ')
    print(a)
    x = a[0] + " " + a[1] + " " + a[2] + " " + a[3] + " " + a[4] + " " + a[5] + " " + a[6] + " " + a[7] + " " + a[8] + " " + a[9]
    print(x)

def task10():
    a = "Нет! Да!"
    b = a * 4
    print(b)

def task11():
    a = input().split(",")
    _1 = int(a[0])
    _2 = int(a[1])
    _3 = int(a[2])
    result = (_1 + _3) // _2
    print(f"result:{result}")

def task12():
    a = input()
    if len(a) < 10:
        print("Введите другое число")
    else:
        print(a[:4])
        print(a[-2:])
        print(a[4:8])
        print(a[::-1])

