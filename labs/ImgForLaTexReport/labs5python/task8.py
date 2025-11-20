import random

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