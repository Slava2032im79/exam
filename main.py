# card = input(' введите номер карты ')
#
#
# def card_number(card):
#     return '*' * len(card[:-4]) + card[-4:]
#
#
# print(card_number(card))


class Tomato:

    states = {0: 'саженец', 1: 'цветение', 2: 'созревание помидора', 3: 'созревший помидор'}
    def __init__(self, index):
        self._index = index
        self._state = 0
    def grow(self):
        self._change_state()
    def is_ripe(self):
        if self._state == 3:
            return True
        return False
    def _change_state(self):
        if self._state < 3:
            self._state += 1
        self._print_state()
    def _print_state(self):
        print(f'Tomato {self._index} is {Tomato.states[self._state]}')
class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(0, num)]
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])
    def give_away_all(self):
        self.tomatoes = []
class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant
    def work(self):
        print('ухаживаем за растениями...')
        self._plant.grow_all()
        print('уход за растениями окончен')
    def harvest(self):
        print('собираем урожай...')
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print('сбор урожая окончен')
        else:
            print('пока рано ,помидоры еще зеленые.')
if __name__ == '__main__':
    great_tomato_bush = TomatoBush(4)
    gardener = Gardener('Emilio', great_tomato_bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()