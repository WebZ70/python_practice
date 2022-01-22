from weapon import Weapon
import random


# Оружие - Лук
# Возможный урон можно узнать, вызвав функцию get_damage.
# Возможный урон - произведение шанса (или точности) и урона оружия.
# При нанесении урона (вызове функции deal_damage) учитывается шанс попадания.
# Шанс попадания хранится в accuracy. Число должно быть в отрезке [0.0, 1.0]
class Bow(Weapon):
    def __init__(self, name, damage, accuracy):
        Weapon.__init__(self, name, damage)
        self.accuracy = accuracy

    def get_damage(self):
        return self.damage * self.accuracy

    def deal_damage(self):
        r = random.random()
        if r <= self.accuracy:
            return self.damage
        return 0

    # Блок геттеров
    @property
    def accuracy(self):
        return self.__accuracy

    # Блок сеттеров
    @accuracy.setter
    def accuracy(self, accuracy):
        self.__accuracy = accuracy
