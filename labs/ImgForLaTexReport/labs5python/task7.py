def task_7():
    rus = {"Russian":"Русский", "Doctor":"Доктор", "Piggy":"Свинка", "cucumber":"Огурец"}
    a = input("Введите русские слова:")
    c = None
    for key, value in rus.items():
        if value == a:
            c = key
    if c:
        print(c)
    else:
        print("В словаре отсутсвует перевод этого слова")