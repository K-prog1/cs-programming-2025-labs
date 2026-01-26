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
        needed = self.level * 50
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
            print("2. +1 Защиты")
            print("3. +1 Атаки")
            print("4. +1 Ловкости")
            
            choice = input("Выбор (1-4): ").strip()
            if choice == "1":
                self.max_health += 5
                self.health += 5  
                self.stat_points -= 1
            elif choice == "2":
                self.defense += 1
                self.stat_points -= 1
            elif choice == "3":
                self.damage += 1
                self.stat_points -= 1
            elif choice == "4":
                self.agility += 1
                self.stat_points -= 1
            else:
                print("Цифру от 1 до 4, мудила!")