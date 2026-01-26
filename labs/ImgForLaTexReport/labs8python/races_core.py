import random

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