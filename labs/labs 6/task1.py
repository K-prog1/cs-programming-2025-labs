time = input("Введите число, систему исчесления числа" \
"и си в которую собираетесь перевести: ")

time1, time2 = time.split(" ")


def TransMut(a,b):
    if a[-1] == 'h' and b == 'm':
        return print(int(a[:-1])*60)
    if time1[-1] == 'm' and time2 =='h':
        return print(int(a[:-1])/60)
    
TransMut(time1,time2)

