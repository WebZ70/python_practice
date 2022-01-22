from weapon import Weapon
import random


# Оружие - Меч
# Возможный урон можно узнать, вызвав функцию get_damage.
# Возможный урон - произведение прочности и урона оружия.
# При нанесении урона (вызове функции deal_damage) учитывается прочность.
# При нанесении удара оружие теряет 10% своей прочности с 50% вероятностью
class Sword(Weapon):
    def __init__(self, name, damage, durability):
        Weapon.__init__(self, name, damage)
        self.durability = durability

    def get_damage(self):
        return self.damage * self.durability

    def deal_damage(self, r=random.random()):
        out_damage = self.get_damage()
        if r >= 0.5:
            self.durability = self.durability - 0.1
        return out_damage

    # Блок геттеров
    @property
    def durability(self):
        return self.__durability

    # Блок сеттеров
    @durability.setter
    def durability(self, durability):
        self.__durability = durability
