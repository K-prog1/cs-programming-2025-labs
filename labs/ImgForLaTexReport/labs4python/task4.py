def task_4():
    number = input("Введите любое число :")
    summa = sum(map(int,list(number)))
    if summa % 3 == 0 and (int(number)%10)%2 == 0:
        print("Число делиться на 3!")
    else:
        print("Не делиться на 3")