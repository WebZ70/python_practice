from __future__ import annotations


class Warrior(object):
    def __init__(self, name, hp=100, ap=1):
        self.name = name
        self.health = hp
        self.attack = ap
        self.state = 'normal'
        self.state_count = 0
        self.armor = None
        self.arsenal = list()
        if len(self.arsenal) > 0:
            list.sort(self.arsenal, reverse=True)

    def __del__(self):
        print("<death> %s отправляется в Вальгаллу" % self.name)

    def get_hit(self, enemy: Warrior, damage, weapon=None, enchant=None):
        if weapon is None:
            if self.armor is None or self.armor.hp == 0:
                print("<fight> %s (%0.1f hp) <--%0.1f-- %s" % (self.name, self.health, damage, enemy.name))
            else:
                print("<fight> %s (%0.1f hp + %0.1f arm) <--%0.1f-- %s" % (
                    self.name, self.health, self.armor.hp, damage, enemy.name))
        else:
            if self.armor is None or self.armor.hp == 0:
                print("<fight> %s (%0.1f hp) <--%0.1f-- %s (%s)" % (self.name, self.health, damage, enemy.name, weapon))
            else:
                print("<fight> %s (%0.1f hp + %0.1f arm) <--%0.1f-- %s (%s)" % (
                    self.name, self.health, self.armor.hp, damage, enemy.name, weapon))

        if self.armor is None:
            self.health = self.health - damage
        else:
            if self.armor.hp > 0:
                self.armor.damage(damage)
            else:
                self.health = self.health - damage

        if self.armor is not None and self.check_armor(enchant):
            self.set_state_count(enchant, 2)

    def deal_damage(self, target: Warrior):
        if self.can_attack():
            damage = 0
            weapon_name = None
            enchant = None
            if len(self.arsenal) > 0:
                damage = self.arsenal[0].deal_damage()
                weapon_name = self.arsenal[0].name
                enchant = self.arsenal[0].enchant
                self.drop_weapon(self.arsenal[0])
                list.sort(self.arsenal, reverse=True)
            if damage < self.attack:
                damage = self.attack

            target.get_hit(self, damage, weapon_name, enchant)

    def drop_weapon(self, weapon):
        if weapon.durability <= 0:
            self.arsenal.remove(weapon)

    def check_death(self):
        return self.health <= 0

    def loot_weapon(self, loot=[]):
        self.arsenal.extend(loot)
        list.sort(self.arsenal, reverse=True)
        for item in loot:
            print('<loot>\t%s подбирает %s!' % (self.name, item.name))

    def print_arsenal(self):
        print("Инвентарь %s:" % self.name)
        if len(self.arsenal) == 0:
            print('\tПуст')
        for item in self.arsenal:
            print("\t<%s> dps=%d" % (item.name, item.get_damage()))

    def check_armor(self, damage_type):
        return self.armor.check_resist(damage_type)

    def can_attack(self):
        if self.state == 'normal':
            return True
        elif self.state == 'burn':
            print("<state>\t%s обьят пламенем! Осталось %d ходов!" % (self.name, self.state_count))
            self.health = self.health - 0.05 * self.health
            self.state_count = self.state_count - 1
            if self.state_count == 0:
                self.state = 'normal'
            return True
        elif self.state == 'freeze':
            print("<state>\t%s заморожен! Осталось %d ходов!" % (self.name, self.state_count))
            self.state_count = self.state_count - 1
            if self.state_count == 0:
                self.state = 'normal'
            return False

    def set_state_count(self, st='normal', r=0):
        print("<state> \t%s получил статус %s на %d хода!" % (self.name, st, r))
        self.state = st
        self.state_count = r

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

    @property
    def arsenal(self):
        return self.__arsenal

    @property
    def state(self):
        return self.__state

    @property
    def state_count(self):
        return self.__state_count

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

    @arsenal.setter
    def arsenal(self, ars):
        self.__arsenal = ars

    @state.setter
    def state(self, st):
        self.__state = st

    @state_count.setter
    def state_count(self, st):
        self.__state_count = st
