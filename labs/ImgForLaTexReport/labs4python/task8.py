def task_8():
    sum = int(input(("Введите сумму товара: ")))
    if sum < 1000:
        print("Ваша скидка: 0%")
        print(sum - ((sum/100)*0))
    if 1000 <= sum < 5000:
        print("Ваша скидка: 5%")
        print(sum - ((sum/100)*5))
    if 5000 <= sum < 10000:
        print("Ваша скидка: 10%")
        print(sum - ((sum/100)*10))
    if sum >= 10000:
        print("Ваша скидка: 15%")
        print(sum - ((sum/100)*15))
    