import random

# === Враги — часть 2 ===

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
    enemy.health += floor * 5
    enemy.damage += floor * 2
    enemy.exp_reward += floor * 3
    return enemy