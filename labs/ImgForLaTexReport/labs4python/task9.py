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