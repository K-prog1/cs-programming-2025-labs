def task_1():
    spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(spisok)):
        if spisok[i] == 3:
            spisok[i] = 30
    print(spisok)