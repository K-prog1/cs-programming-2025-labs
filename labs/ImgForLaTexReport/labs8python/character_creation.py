# Этот файл подключается в main_game.py
# Логика выбора расы и генерации характеристик уже встроена в main_game.py
# Но если выделить отдельно:

def create_character(choice, name):
    if choice == "1":
        player = Absorber(name)
    elif choice == "2":
        player = Ghoul(name)
    else:
        player = Awake(name)
    return player