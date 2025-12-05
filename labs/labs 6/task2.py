def bank_sistem():
    god_stavka = 0
    bonus_stavki = 0
    print("минимальный вклад 30000 рублей.")
    vklad = input("Сделайте вклад указав срок в годах, на который собираетесь его класть: ").split(' ')
    vkladint0 = int(vklad[0]) 
    vkladint1 = int(vklad[1])
    if vkladint0 < 30000:
        print("Вклад не может быть меньше 30000 рублей")
        return 
    else:
        
        for i in range(1, vkladint1):
            if i <= 3:
                bonus_stavki = 0.03
            elif 4 <= i < 6:
                bonus_stavki = 0.05
            elif i >= 6:
                bonus_stavki = 0.02

        vkladint0 = vkladint0 + vkladint0 * bonus_stavki
        c = vkladint0

        while (c >= 10000) and (god_stavka < 5):
            c -= 10000
            god_stavka += 0.003

        vkladint0 += vkladint0* bonus_stavki
    print(vkladint0)

bank_sistem()

        
            


    