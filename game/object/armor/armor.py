import random

class Armor:
    def __init__(self, name, hp=100, enchant='normal', power=1.0):
        self.name = name
        self.enchant = enchant
        self.hp = hp
        self.power = power

    def damage(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0

    def check_resist(self, damage_type):
        r = random.random()
        if self.enchant == 'normal':
            return False
        elif (self.enchant == 'burn' or self.enchant == 'burnfreeze') and damage_type == 'burn':
            return r <= self.power
        elif (self.enchant == 'freeze' or self.enchant == 'burnfreeze') and damage_type == 'freeze':
            return r <= self.power

    # Блок геттеров
    @property
    def name(self):
        return self.__name

    @property
    def enchant(self):
        return self.__enchant

    @property
    def hp(self):
        return self.__hp

    @property
    def power(self):
        return self.__power

    # Блок сеттеров
    @name.setter
    def name(self, name):
        self.__name = name

    @enchant.setter
    def enchant(self, enchant):
        self.__enchant = enchant

    @hp.setter
    def hp(self, hp):
        self.__hp = hp

    @power.setter
    def power(self, power):
        self.__power = power
