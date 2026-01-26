import random

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

def conduct_battle(player, enemy, inventory, floor):
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
                return
            else:
                print("Не вышло... Они тебя настигли!")
        else:
            print("Пропуск хода!")

        if enemy.is_alive():
            print(f"\n--- ХОД ВРАГА ---")
            enemy.attack(player)
            player.update_effects()

    if player.is_alive():
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