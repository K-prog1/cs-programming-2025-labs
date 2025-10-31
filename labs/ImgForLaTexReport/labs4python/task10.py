def task_10():
    a = 0
    chislo = int(input("Введите число: "))
    for i in range(2, 9 + 1):
        if chislo % i != 0:
            a += 1
    if a == 8:
        print(f"{chislo} - простое число")
    else:
        print(f"{chislo} - составное число")