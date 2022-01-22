from object.warrior import Warrior
from object.weapon.sword import Sword
from object.weapon.bow import Bow
from object.armor.armor import Armor
import random


def battle():
    list_of_weapon = [
        Sword('Frostmourne', 2, 1),
        Sword('Hammer of Doom', 30, 0.5),
        Bow('Crossbow', 2, 1, 0.8),
        Bow('Infinite Throwing Javelin', 30, 0.2, 1)
    ]
    list_of_armor = [
        Armor('Ranger Armor', 100),
        Armor('Reinforced Armor', 1, 'freeze'),
        Armor('Enchanted Shirt', 10, 'burn'),
        Armor('Cloak Of Invisibility', 50, 'burnfreeze')
    ]
    list_of_war = [
        Warrior('Arthas', 50, 10),
        Warrior('Uther', 50, 10),
        Warrior('Jaina', 50, 10),
        Warrior('Thrall', 50, 10),
        Warrior('Kael', 50, 10),
        Warrior('Illidan', 50, 10)
    ]

    print('\t\t Бой скоро начнется! Готовтесь!')
    print('На поле битвы:')
    for challenger in list_of_war:
        print('\t%s с атакой равной %d' % (challenger.name, challenger.attack))

    print('\n')
    for weapon in list_of_weapon:
        r1 = random.choice(list_of_war)
        r1.loot_weapon([weapon])

    for armor in list_of_armor:
        r1 = random.choice(list_of_war)
        while r1.armor is not None:
            r1 = random.choice(list_of_war)
        r1.armor = armor

    print('\n\t\t В бой!\n')
    print('========== Журнал боя ==========')
    while len(list_of_war) > 1:
        r1 = random.randint(0, len(list_of_war) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(list_of_war) - 1)

        list_of_war[r1].deal_damage(list_of_war[r2])
        if list_of_war[r2].check_death():
            list_of_war[r1].loot_weapon(list_of_war[r2].arsenal)
            del list_of_war[r2]
    print('================================')
    print('\n\t\t Бой окончен!')
    print('\tПобеждает %s!' % list_of_war.pop().name)
