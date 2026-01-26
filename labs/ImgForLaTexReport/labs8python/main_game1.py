import random

# ======================
# ОСНОВНАЯ ИГРА
# ======================

def main():
    print("💀 ДОБРО ПОЖАЛОВАТЬ В ПОДЗЕМЕЛЬЕ БОЛИ 💀")
    print("Только сильнейшие выживут. Остальные — корм для пингвинов.\n")

    print("Выбери свою суть:")
    print("1. Поглотитель (впитывает урон и выплёскивает обратно)")
    print("2. Гуль (лечится при каждой атаке)")
    print("3. Пробуждённый (становится сильнее в бою)")
    
    while True:
        choice = input("Твой выбор (1-3): ").strip()
        if choice in ("1", "2", "3"):
            break
        print("Цифру!")

    name = input("Имя твоего аватара боли: ").strip() or "Безымянный"

    if choice == "1":
        player = Absorber(name)
    elif choice == "2":
        player = Ghoul(name)
    else:
        player = Awake(name)

    print(f"\n {player.name}, {player.race}")
    print("Перед тобой бесконечные коридоры... Выбирай путь!\n")

    floor = 1
    room = 0
    inventory = Inventory()

    while player.is_alive():
        room += 1
        print(f"\n{'='*50}")
        print(f"ЭТАЖ {floor} • КОМНАТА {room}")
        print(f"HP: {player.health}/{player.max_health} | Урон: {player.total_attack}")

        left_room = random.choice(["enemy", "chest", "rest"])
        right_room = random.choice(["enemy", "chest", "rest"])

        left_known = random.choice([True, False])
        right_known = random.choice([True, False])

        print("\nПеред тобой развилка:")
        left_desc = left_room if left_known else "???"
        right_desc = right_room if right_known else "???"
        print(f"(1) СЛЕВА: {left_desc}")
        print(f"(2) СПРАВА: {right_desc}")

        while True:
            path = input("\nКуда двинешь? (1/2): ").strip()
            if path in ("1", "2"):
                break
            print("1 или 2, епта!")

        chosen_room = left_room if path == "1" else right_room

        if chosen_room == "enemy":
            enemy = generate_enemy(floor)
            print(f"\n⚔️  ВЫЗОВ! {enemy.name} бросает тебе вызов!")
            
            while player.is_alive() and enemy.is_alive():
                print("\n--- ТВОЙ ХОД ---")
                print("1. Атаковать")
                print("2. Использовать предмет")
                print("3. Сбежать (50%)")
                
                action = input("Действие: ").strip()
                
                if action == "1":
                    player.attack(enemy)
                    enemy.update_effects()
                elif action == "2":
                    inventory.show()
                    if inventory.items:
                        try:
                            idx = int(input("Номер предмета (0 — отмена): "))
                            if idx > 0:
                                inventory.use_item(idx, player)
                            continue 
                        except ValueError:
                            print("Число давай!")
                            continue
                    else:
                        print("Инвентарь пуст!")
                        continue
                elif action == "3":
                    if random.random() < 0.5:
                        print("Ты сбежал, как крыса!")
                        break
                    else:
                        print("Не вышло... Они тебя настигли!")
                else:
                    print("Пропуск хода!")

                if enemy.is_alive():
                    print(f"\n--- ХОД ВРАГА ---")
                    enemy.attack(player)
                    player.update_effects()

            if player.is_alive() and not enemy.is_alive():
                print(f"\n Победа! Получено {enemy.exp_reward} опыта.")
                player.gain_exp(enemy.exp_reward)
                inventory.gold += random.randint(5, 15)
                
                if random.random() < 0.4:
                    loot = generate_loot()
                    if loot["type"] == "gold":
                        inventory.gold += loot["amount"]
                        print(f"Найдено {loot['amount']} золота!")
                    else:
                        inventory.add_item(loot)

        elif chosen_room == "chest":
            print("\nСУНДУК! Что внутри?")
            loot = generate_loot()
            if loot["type"] == "gold":
                inventory.gold += loot["amount"]
                print(f"Найдено {loot['amount']} золота!")
            else:
                inventory.add_item(loot)

        elif chosen_room == "rest":
            print("\nТИШИНА... Ты отдыхаешь.")
            player.health = player.max_health
            print("HP восстановлено полностью!")
            if player.stat_points > 0:
                player.apply_statpoints()

        if room % 4 == 0:
            floor += 1
            print(f"\n ТЫ СПУСТИЛСЯ НА ЭТАЖ {floor}! Враги стали ЖЕСТЧЕ.")

    print(f"\n💀 {player.name} пал в подземелье...")
    print("Но легенда о нём будет жить вечно.")


# Генерация предметов (перенесена сюда для полноты)
def generate_loot():
    loot_pool = [
        {"name": "Зелье лечения", "type": "potion", "heal": 25},
        {"name": "Меч новичка", "type": "weapon", "attack": 5},
        {"name": "Стальной меч", "type": "weapon", "attack": 8},
        {"name": "Кожаная броня", "type": "armor", "defense": 3},
        {"name": "Кольчуга", "type": "armor", "defense": 5},
        {"name": "Монеты", "type": "gold", "amount": random.randint(10, 30)}
    ]
    return random.choice(loot_pool)

if __name__ == "__main__":
    main()