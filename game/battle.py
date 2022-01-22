from classes import Warrior
import random


def battle():
    list_of_war = [Warrior('Arthas', 3), Warrior('Uther', 3), Warrior('Jaina', 3)]

    print('\t\t Бой скоро начнеться! Готовтесь!')
    print('На поле :')
    
    for obj in list_of_war:
        print('\t%s с уроном %d' % (obj.get_name(), obj.get_attack()))

    print('\n\t\t В бой!\n')
    print('++++++++++ Журнал боя ++++++++++')

    while len(list_of_war) > 1:
        r1 = random.randint(0, len(list_of_war) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(list_of_war) - 1)

        list_of_war[r1].get_hit(list_of_war[r2])
        if list_of_war[r1].check_death():
            del list_of_war[r1]
 
    print('++++++++++++++++++++++++++++++')
    print('\n\t\t Битва окончена!')
    print('\tПобеждает %s!' % (list_of_war.pop().get_name()))

