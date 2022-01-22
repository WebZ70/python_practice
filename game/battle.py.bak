from classes import Warrior as War
import random


def battle():
    list_of_war = [War('Sonic', 3), War('Tales', 3), War('Knuckles', 3)]

    print('\t\t Турнир начался!')
    print('Бойцы на арене:')
    for challenger in list_of_war:
        print('\t%s с атакой равной %d' % (challenger.name, challenger.attack))

    print('\n\t\t Начать битву!\n')
    print('========== Журнал боя ==========')
    while len(list_of_war) > 1:
        r1 = random.randint(0, len(list_of_war) - 1)
        r2 = r1
        while r1 == r2:
            r2 = random.randint(0, len(list_of_war) - 1)

        list_of_war[r1].get_hit(list_of_war[r2])
        if list_of_war[r1].check_death():
            del list_of_war[r1]
    print('================================')
    print('\n\t\t Турнир окончен!')
    print('\tПобеду одерживает %s!' % list_of_war.pop().name)
    print('\tНо герои не живут вечно!')
