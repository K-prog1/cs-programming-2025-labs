def task_5():
    problem_password = []
    password = input("ВВедите пароль: ")
    spec_simvols = ".,:;!_*-+()/#¤%&"

    has_upper = False
    has_lower = False
    has_number = False
    has_spec_simvols = False
    len_passsword = False

    if len(password) >= 8:
        len_passsword = True
    else:
        problem_password.append("8 символов в коде")

    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True 
        if i.isdigit():
            has_number = True
        if i in spec_simvols:
            has_spec_simvols = True
    if (len_passsword and has_lower and has_number and has_spec_simvols and has_upper) == True:
        print("Пароль надежный! Он подходит")
    
    else:
        if not has_lower:
            problem_password.append("строчных букв")
        if not has_number:
            problem_password.append("цифр")
        if not has_spec_simvols:
            problem_password.append("спец символов")
        if not has_upper:
            problem_password.append("отсутствуют заглавные")
        print(f"У вас отсутствуют: {", ".join(problem_password)}") 