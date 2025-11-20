def task_5():
    dicto = {"Молоко":1000, "Пепси-кола":1, "Мясо козла":9999}
    highest_price = max(dicto, key = dicto.get)
    lowest_price = min(dicto, key = dicto.get )
    print("Самый дорогой товар:", highest_price,"-", dicto[highest_price])
    print("Самый дешевый товар:", lowest_price,"-", dicto[lowest_price])
