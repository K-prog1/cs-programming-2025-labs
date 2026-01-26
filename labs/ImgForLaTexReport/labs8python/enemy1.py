import random

# === Враги — часть 1 ===

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