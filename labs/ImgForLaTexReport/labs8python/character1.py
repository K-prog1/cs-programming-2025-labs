import random

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