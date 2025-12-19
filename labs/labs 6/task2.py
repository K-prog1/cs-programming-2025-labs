def bank_sistem():
    god_stavka = 0
    bonus_stavki = 0
    print("минимальный вклад 30000 рублей.")
    try:
        vklad = input("Сделайте вклад указав срок в годах, на который собираетесь его класть: ").split(' ')
        vkladint0 = int(vklad[0]) 
        vkladint1 = int(vklad[1])
    except:
        print("Введите значения через пробел")

    if vkladint0 < 30000:
        print("Вклад не может быть меньше 30000 рублей")
    else:
    
        c = vkladint0
        god_stavka = 0
        while (c >= 10000) and (god_stavka < 0.05):
            c -= 10000
            god_stavka += 0.003

        if vkladint1 <= 3:
            bonus_stavki = 0.03
        elif 4 <= vkladint1 <= 6:
            bonus_stavki = 0.05
        elif vkladint1 >= 6:
            bonus_stavki = 0.02
    
    summa_stavok = god_stavka + bonus_stavki
    vkladint2 = vkladint0

    for god in range(vkladint1):
        vkladint2 = vkladint2 *(1+summa_stavok)

    vkladint3 = vkladint2 - vkladint0
                        
    print(vkladint3)

bank_sistem()

        
            


    