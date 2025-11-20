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
<<<<<<< Updated upstream

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
        


=======
>>>>>>> Stashed changes

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

    words = ["яблоко", "груша", "банан", "киви", "апельсин", "ананас"]
    result = {}

    for word in words:

        first_letter = word[0]

        if first_letter not in result:

            result[first_letter] = []
    
        result[first_letter].append(word)

    print(result)

task_9()

def task_10():
    students = [("Анна", [5, 4, 5]), ("Иван", [3, 4, 4]), ("Мария", [5, 5, 5])]
    average_grades = {}

    for name, grades in students:
        average = sum(grades) / len(grades)
        average_grades[name] = average

    print("Словарь со средними оценками:")
    print(average_grades)


    best_student = None
    best_average = 0

    for name, average in average_grades.items():
        if average > best_average:
            best_average = average
            best_student = name

    print(f"\nСтудент с наибольшей средней оценкой:")
    print(f"Имя: {best_student}, Средний балл: {best_average}")