from object.weapon.weapon import Weapon
import random


# Оружие - Меч
# Возможный урон можно узнать, вызвав функцию get_damage.
# Возможный урон - произведение прочности и урона оружия.
# При нанесении урона (вызове функции deal_damage) учитывается прочность.
# При нанесении удара оружие теряет 10% своей прочности с 50% вероятностью
class Sword(Weapon):
    def __init__(self, name, damage, durability, enchant='normal'):
        Weapon.__init__(self, name, damage, durability, enchant)

    def get_damage(self):
        if self.durability > 0:
            return self.damage * self.durability
        else:
            return 0

    def deal_damage(self, r=random.random()):
        out_damage = self.get_damage()
        if r >= 0.5:
            self.durability = self.durability - 0.1
        if self.durability <= 0:
            print('<weapon>\t%s почти сломано!' % self.name)
        return out_damage
