import random

# === Персонаж и действия ===

class Character:
    def __init__(self, name, race, health, damage, defense, agility, height, weight):
        self.name = name
        self.race = race
        self.health = health          
        self.max_health = health      
        self.damage = damage
        self.defense = defense
        self.agility = agility
        self.height = height          
        self.weight = weight          
        
        self.level = 1
        self.exp = 0
        self.stat_points = 0

        self.weapon_name = "Палка"
        self.weapon_attack = 0
        self.armor_name = "Бандаж"
        self.armor_defense = 0

        self.effects = []

    @property
    def index_mass(self):
        height_m = self.height / 100
        return self.weight / (height_m ** 2)

    @property
    def total_attack(self):
        return self.damage + self.weapon_attack

    @property
    def total_defense(self):
        imt = self.index_mass
        bonus_defense = 0
        if imt < 18.5:
            bonus_defense = -3  
        elif imt > 25:
            bonus_defense = 5   
        return self.defense + self.armor_defense + bonus_defense

    @property
    def evasion_chance(self): 
        base_dodge = self.agility / 100  
        imt = self.index_mass
        bonus_dodge = 0
        if imt < 18.5:
            bonus_dodge = 0.2  
        elif 18.5 <= imt <= 25:
            bonus_dodge = 0.05  
        else: 
            bonus_dodge = -0.15 
        total = base_dodge + bonus_dodge
        return max(0.0, min(0.7, total))  

    def apply_effect(self, effect_name, duration, damage_per_turn=0):
        self.effects.append({
            "name": effect_name,
            "duration": duration,
            "damage_per_turn": damage_per_turn
        })

    def update_effects(self):
        new_effects = []
        for effect in self.effects:
            if effect["duration"] > 0:
                if effect["damage_per_turn"] > 0:
                    print(f"  → {self.name} получает {effect['damage_per_turn']} урона от '{effect['name']}'")
                    self.take_damage(effect["damage_per_turn"])
                effect["duration"] -= 1
                new_effects.append(effect)
            else:
                print(f"  → Эффект '{effect['name']}' закончился.")
        self.effects = new_effects

    def take_damage(self, damage):
        if random.random() < self.evasion_chance:
            print(f"  → {self.name} уклонился!")
            return 0

        actual_damage = max(1, damage - self.total_defense)
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        print(f"  → {self.name} получил {actual_damage} урона. Здоровье: {self.health}")
        return actual_damage  

    def attack(self, other):
        print(f"{self.name} бьёт {other.name}!")
        other.take_damage(self.total_attack)

    def is_alive(self):
        return self.health > 0

    def heal(self, amount):
        old_health = self.health
        self.health = min(self.max_health, self.health + amount)
        healed = self.health - old_health
        print(f"  → {self.name} восстановил {healed} HP. Теперь HP: {self.health}")

    def gain_exp(self, amount):
        self.exp += amount
        needed = self.level * 10 
        if self.exp >= needed:
            self.level_up()
    
    def level_up(self):
        self.level += 1
        self.stat_points += 3
        print(f"\n🔥 Уровень повышен! Теперь у вас {self.level}-й уровень. Получено 3 очка характеристик.")
        self.apply_statpoints()

    def apply_statpoints(self):
        while self.stat_points > 0:
            print(f"\nУ вас {self.stat_points} очко(а/ов). Куда вложите?")
            print("1. +5 Здоровья")
            print("2. +3 Защиты")
            print("3. +3 Атаки")
            print("4. +3 Ловкости")
            
            choice = input("Выбор (1-4): ").strip()
            if choice == "1":
                self.max_health += 5
                self.health += 5  
                self.stat_points -= 1
            elif choice == "2":
                self.defense += 3
                self.stat_points -= 1
            elif choice == "3":
                self.damage += 3
                self.stat_points -= 1
            elif choice == "4":
                self.agility += 3
                self.stat_points -= 1
            else:
                print("Цифру от 1 до 4, мудила!")


# === Инвентарь ===
class Inventory:
    def __init__(self, capacity=10):
        self.items = []
        self.capacity = capacity
        self.gold = 0
        
    def add_item(self, item):
        if len(self.items) >= self.capacity:
            print("Сори инвентарь полон, попробуй что-то выкинуть:")
            self.show()
            idx = input("Номер предмета для выброса (0-ничего): ")
            if idx.isdigit() and 1 <= int(idx) <= len(self.items):
                self.items.pop(int(idx)-1)
            else:
                print("Предмет не добавлен")
                return False
        self.items.append(item)
        print(f"Получен предмет: {item.get('name', '???')}")
        return True
    
    def show(self):
        print("\n----Инвентарь----")
        print(f"Золото: {self.gold}")
        if not self.items:
            print("Пусто.")
        else:
            for i, item in enumerate(self.items, 1):
                print(f"{i}. {item['name']}")

    def use_item(self, index, character):
        if 1 <= index <= len(self.items):
            item = self.items[index - 1]
            if item["type"] == "potion":
                character.heal(item["heal"])
                self.items.pop(index - 1)
            elif item["type"] == "weapon":
                old_name, old_atk = character.weapon_name, character.weapon_attack
                character.weapon_name = item["name"]
                character.weapon_attack = item["attack"]
                self.items.pop(index - 1)
                if old_name != "Палка":
                    self.items.append({"name": old_name, "type": "weapon", "attack": old_atk})
                print(f"Экипировано: {item['name']}")
            elif item["type"] == "armor":
                old_name, old_def = character.armor_name, character.armor_defense
                character.armor_name = item["name"]
                character.armor_defense = item["defense"]
                self.items.pop(index - 1)
                if old_name != "Бандаж":
                    self.items.append({"name": old_name, "type": "armor", "defense": old_def})
                print(f"Экипировано: {item['name']}")
            else:
                print("Нельзя использовать.")
        else:
            print("Нет такого предмета!")


# === Враги ===
class Enemy(Character):
    def __init__(self, name, hp, attack, defense, agility, height=170, weight=60):
        super().__init__(name, "Монстр", hp, attack, defense, agility, height, weight)
        self.exp_reward = 0

    def set_exp(self, exp):
        self.exp_reward = exp

    def special_ability(self, target):
        pass

    def attack(self, other):
        print(f"{self.name} бьёт {other.name}!")
        other.take_damage(self.total_attack)
        if random.random() < 0.3:  
            self.special_ability(other)


class PingVin735(Enemy):
    def __init__(self):
        super().__init__("Пингвин", 25, 6, 1, 40, 100, 20)
        self.set_exp(15)

    def special_ability(self, target):
        print(f"  → {self.name} ударил клювом! {target.name}!")
        target.apply_effect("Кровотечение", duration=2, damage_per_turn=3)


class AlwaysComeBack(Enemy):
    def __init__(self):
        super().__init__("Человек в маске", 200, 20, 10, 10, 200, 120)
        self.set_exp(100)
        self.resurrection_used = False
        self.resurrect_chance = 0.6

    def take_damage(self, damage):
        actual = super().take_damage(damage)
        if self.health <= 0 and not self.resurrection_used:
            if random.random() < self.resurrect_chance:
                self.resurrection_used = True
                self.health = self.max_health // 2 
                print(f"💀 {self.name} пал... но ВОСКРЕС!")
                print(f"🔥 {self.name} теперь имеет {self.health} HP!")
            else:
                print(f"💀 {self.name} окончательно уничтожен.")
        return actual


class Regenerator(Enemy):
    def __init__(self):
        super().__init__("Регенератор", 60, 15, 4, 45, 150, 40)
        self.set_exp(30)

    def special_ability(self, target):
        self.heal(8)


class Vsosun(Enemy):
    def __init__(self):
        super().__init__("Всасыватель", 100, 20, 2, 10, 170, 65)
        self.set_exp(50)

    def special_ability(self, target):
        heal = min(10, target.damage // 2)
        self.health += heal
        print(f"  → {self.name} высасывает {heal} HP из {target.name}!")


class PowerUpper(Enemy):
    def __init__(self):
        super().__init__("Неизвестный", 50, 5, 10, 50, 170, 60)
        self.set_exp(70)

    def special_ability(self, target):
        old_damage = self.damage
        self.damage = int(self.damage * 1.5)
        print(f"  → {self.name} вы видите, как у него неожиданно появляются мышцы...")
        print(f"  → Урон: {old_damage} → {self.damage}")


def generate_enemy(floor):
    enemies = [Vsosun(), Regenerator(), PowerUpper(), AlwaysComeBack(), PingVin735()]
    enemy = random.choice(enemies)
    # Усиление с этажом
    enemy.health += floor * 5
    enemy.damage += floor * 2
    enemy.exp_reward += floor * 3
    return enemy


# === Генерация предметов ===
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


# === РАСЫ ===
class Absorber(Character):
    def __init__(self, name):
        hp = random.randint(110, 130)
        attack = random.randint(14, 16)
        defense = random.randint(7, 9)
        agility = random.randint(28, 32)
        height = random.randint(180, 200)
        weight = random.randint(80, 90)
        super().__init__(name, "Поглотитель", hp, attack, defense, agility, height, weight)
        self.absorbed_damage = 0 

    def take_damage(self, damage):
        if random.random() < self.evasion_chance:
            print(f"  → {self.name} уклонился!")
            return 0

        actual_damage = max(1, damage - self.total_defense)
        absorbed = actual_damage // 2
        real_taken = actual_damage - absorbed

        self.absorbed_damage += absorbed
        self.health -= real_taken
        if self.health < 0:
            self.health = 0

        print(f"  → {self.name} поглотил {absorbed} урона! Получил только {real_taken}.")
        print(f"  → Накоплено для выплеска: {self.absorbed_damage}")
        return actual_damage

    def attack(self, other):
        base_dmg = self.total_attack
        bonus_dmg = self.absorbed_damage

        if bonus_dmg > 0:
            total_dmg = base_dmg + bonus_dmg
            print(f"{self.name} бьёт {other.name} с силой {base_dmg} + {bonus_dmg} (накопленного)!")
            other.take_damage(total_dmg)
            self.absorbed_damage = 0  
        else:
            print(f"{self.name} бьёт {other.name}!")
            other.take_damage(base_dmg)


class Ghoul(Character):
    def __init__(self, name):
        hp = random.randint(90, 110)
        attack = random.randint(18, 22)
        defense = random.randint(4, 6)
        agility = random.randint(48, 52)
        height = random.randint(170, 180)
        weight = random.randint(55, 65)
        super().__init__(name, "Гуль", hp, attack, defense, agility, height, weight)
    
    def attack(self, other):
        print(f"{self.name} бьёт {other.name}!")
        other.take_damage(self.total_attack)
        heal_amount = min(8, self.total_attack // 3)
        self.heal(heal_amount)


class Awake(Character): 
    def __init__(self, name):
        hp = random.randint(85, 95)
        attack = random.randint(23, 27)
        defense = random.randint(2, 4)
        agility = random.randint(68, 72)
        height = random.randint(175, 185)
        weight = random.randint(65, 75)
        super().__init__(name, "Пробуждённый", hp, attack, defense, agility, height, weight)
        self.battle_actions = 0 

    def attack(self, other):
        print(f"{self.name} бьёт {other.name}!")
        other.take_damage(self.total_attack)
        self.damage += 2
        self.agility += 1
        self.battle_actions += 1
        print(f"  → {self.name} пробуждается! Атака +2, Ловкость +1")

    def take_damage(self, damage):
        actual = super().take_damage(damage)
        if actual > 0:
            self.defense += 1
            self.battle_actions += 1
            print(f"  → Боль делает {self.name} сильнее! Защита +1")
        return actual


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



if __name__ == "__main__":
    main()