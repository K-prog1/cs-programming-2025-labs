def task_4():
    schet = 0
    kortej = (1, "2", 3, "попа", 66, 43)
    for i in kortej:
        if type(i) is int:
            schet += 1
    if schet == len(kortej):
        print('Все элементы числа')
    else:
        print("В кортежи не только числа")