from object.weapon.bow import Bow
from object.weapon.sword import Sword
from object.warrior import Warrior
import battle

def test():
    bow = Bow('Crossbow', 15, 0.2, 0.5)
    sword1 = Sword('Frost', 15, 0.2)
    sword2 = Sword('Demons Hand', 100, 0.1)

    war1 = Warrior('Warrior1', 100, 1, [sword1, sword2])
    war2 = Warrior('Warrior2', 150, 1, [bow])
    war1.print_arsenal()
    war2.print_arsenal()

    for i in range(10):
        war1.deal_damage(war2)
        if len(war1.arsenal) > 0:
            print('\t'+war1.arsenal[0].name)
        else:
            print('\t С руки')
        if war2.check_death():
            war1.loot_weapon(war2.arsenal)
            del war2
            break

    war1.print_arsenal()

if __name__ == '__main__':
    battle.battle()
    #test()
