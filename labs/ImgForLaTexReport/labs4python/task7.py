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
