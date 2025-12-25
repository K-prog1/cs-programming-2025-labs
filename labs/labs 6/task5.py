def is_poly():
    s = input("Введите строку: ")
    clean = ''.join(ch for ch in s if ch.isalnum()).upper()
    if clean == clean[::-1]:
        print("Все верно!")
    else:
        print("Все плохо!")

is_poly()