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