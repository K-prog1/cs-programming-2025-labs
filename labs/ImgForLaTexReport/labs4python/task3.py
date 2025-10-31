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