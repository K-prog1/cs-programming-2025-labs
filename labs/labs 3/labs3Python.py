def task_1():
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    for i in range(10):
        print(f'My name is {name}. Who? My age is {age}. What?')

def task_2():
    numb = int(input('Введите число от 1 до 9: '))
    if numb <= 9:
        for b in range(1,10):
            print(f'{numb}*{b}= {numb*b}')
    else:
        print("Wasted")

def task_3():
    for i in range(1, 101, 3):
        print(i)


def task_4():
    
    a = 1
    number = int(input('Введите число или цифру: '))
    if number >0:
        for i in range(1, number+1):
            a *= i
            print(a)
    if number == 0:
        print(1)
    else:
        print("Факториала отрицательных- не существует")

def task_5():
    a = 21
    while a != 0:
        a -= 1
        print(a)


def task_6():
    a, b = 0, 1
    for i in range(int(input("Введите число: "))+1):
        print(f"F({i}) = {a}")
        a, b = b, a + b  

def task_7():
    n = input("Введите строку: ")  
    result = ""  
    
    for index, char in enumerate(n):
        result += char + str(index) 
    
    print("Результат:", result)

def task_8():
    while True:
        a = int(input('Введите первое число или цифру: '))
        b = int(input('Введите второе число или цифру: '))
        c = a+b
        print(f"сумма чисел: {c}")
task_8()
        
        

        


    


   


            

            
