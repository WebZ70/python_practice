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
    

            
    print('++++++++++++++++++++++++++++++')
    print('\n\t\t Турнир окончен!')
    print('\tПобеду одерживает %s!' % (list_of_war.pop().get_name()))
    print('\tНо герои не живут вечно!')
