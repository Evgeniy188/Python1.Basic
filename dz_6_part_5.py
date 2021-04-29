class Stationery:

    def __init__(self, t):
        self.title = t

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self):
        super(Pen, self).__init__('pen')

    def draw(self):
        print('Начинаем рисовать', self.title)

class Pencil(Stationery):

    def __init__(self):
        super(Pencil, self).__init__('pencil')

    def draw(self):
        print('Начинаем рисовать', self.title)

class Handle(Stationery):

    def __init__(self):
        super(Handle, self).__init__('handle')

    def draw(self):
        print('Начинаем рисовать', self.title)

marker = Stationery('marker')
pen = Pen()
pencil = Pencil()
handle = Handle()

marker.draw()
pen.draw()
pencil.draw()
handle.draw()



