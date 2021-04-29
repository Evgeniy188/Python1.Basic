import time
from itertools import cycle


class TrafficLight:

    def __init__(self, color=None):
        self.__color = color

    def running(self):
        color_dict = {'red': [3, '\033[1m\033[41m'], 'yellow': [2, '\033[1m\033[43m]'], 'green': [1, '\033[1m\033[42m']}
        start_time = time.time()
        for el, v in cycle(color_dict.items()):
            if time.time() - start_time < 20:
                self.__color = el
                print(v[1] + self.__color)
                time.sleep(v[0])
            else:
                return


tl = TrafficLight()
tl.running()
