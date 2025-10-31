def task_6():
    try:
        year = int(input("Введите год для проверки на его високосность: "))
     
        if ((year % 4 == 0) and (year % 100 !=0)) or year % 400 == 0:
            print(f"{year} - Год високосный")
        else:
            print(f"{year} - Год не високосный")
    except:
        print("Введи цифры, а не чепуху")