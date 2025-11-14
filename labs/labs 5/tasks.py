import random

def task_1():
    spisok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(spisok)):
        if spisok[i] == 3:
            spisok[i] = 30
    print(spisok)

def task_2():
    spisok = [1,2,3,4,5]
    for i in range(len(spisok)):
        spisok[i] = spisok[i]**2

def task_3():
    spisok = [23,55,12,23,7,8,100] 
    print(max(spisok)/len(spisok))

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

def task_5():
    dicto = {"Молоко":1000, "Пепси-кола":1, "Мясо козла":9999}
    highest_price = max(dicto, key = dicto.get)
    lowest_price = min(dicto, key = dicto.get )
    print("Самый дорогой товар:", highest_price,"-", dicto[highest_price])
    print("Самый дешевый товар:", lowest_price,"-", dicto[lowest_price])

def task_6():
    list = ["propan","клертон",'флиртон',123,444,323]
    dict = {}
    for i in list:
        dict[i] = i
    print(dict)
        
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

def task_8():
    data = ["Ножницы", "Бумага", "Ящерица", "Камень", "Спок"]
    HumanInput = input("Введите Камень-Ножницы-Бумага-Ящерица-Спок, что-то одно: ")
    if HumanInput in data:
        rand = random.choice(data)
        if (HumanInput == "Ножницы" and rand == "Бумага") or \
            (HumanInput == "Бумага" and rand == "Камень") \
            or (HumanInput == "Камень" and rand == "Ящерица") \
            or (HumanInput == "Ящерица" and rand == "Спока")\
            or (HumanInput == "Спок" and rand == "Ножницы")\
            or (HumanInput == "Ножницы" and rand == "Ящерица")\
            or (HumanInput == "Ящерица" and rand == "Бумага")\
            or (HumanInput == "Бумага" and rand == "Спок")\
            or (HumanInput == "Спок" and rand == "Камень")\
            or (HumanInput == "Камень" and rand == "Бумага"):
            print("Вы победили")
        else:
            print("Лошпед продул")

    else:
        print("Нету таких значений из перечисленных")


def task_9():
    a = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
        



