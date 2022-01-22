from __future__ import annotations


class Warrior(object):
    def __init__(self, name, hp=100, ap=1):
        self.name = name
        self.health = hp
        self.attack = ap

    def __del__(self):
        print("%s отправляется в Вальгаллу" % self.name)

    def get_hit(self, enemy: Warrior):
        self.health = self.health - enemy.attack
        print("%s получил %d урона от %s" % (self.name, enemy.attack, enemy.name))

    def check_death(self):
        return self.health <= 0

    # Блок геттеров
    @property
    def attack(self):
        return self.__attack

    @property
    def health(self):
        return self.__health

    @property
    def name(self):
        return self.__name

    # Блок сеттеров
    @attack.setter
    def attack(self, ap):
        self.__attack = ap

    @health.setter
    def health(self, hp):
        self.__health = hp

    @name.setter
    def name(self, n):
        self.__name = n
