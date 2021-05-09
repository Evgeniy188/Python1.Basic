class Store:

    def __init__(self, name, size):
        self.data = {}
        self.name = name
        self.max_size = size
        self.size = 0

    def add_to(self, eq):
        if self.size + eq.size * eq.count <= self.max_size:
            self.size += eq.size * eq.count
            if eq.title in self.data.keys():
                self.data[eq.title].count += eq.count
            else:
                self.data.update({eq.title: eq})
        else:
            print('Невозможно добавить товар. Склад переполнен')

    def give_out(self, eq):
        if eq.title in self.data.keys():
            if eq.count > self.data[eq.title].count:
                print(f'Недостаточно товара на складе. Осталось {self.data[eq.title].count} шт.')
            else:
                self.size -= eq.size * eq.count
                self.data[eq.title].count -= eq.count
                if self.data[eq.title].count == 0:
                    self.data.pop(eq.title)
                return eq
        else:
            print('Товара нет на складе.')

    def info(self):
        print(f'На складе {self.name} в наличии:')
        [print(v) for i, v in self.data.items()]
        print(f'Осталось места: {self.max_size - self.size}')

class OfficeEq:

    def __init__(self, title, price, count, size):
        self.title = title
        self.price = price
        self.count = count
        self.size = size

    def __str__(self):
        return f'{self.title} - {self.count}'


class Printer(OfficeEq):

    def __init__(self, title, price, count, size, color=False):
        super().__init__(title, price, count, size)
        self.color = color

    def __str__(self):
        color = 'цветной' if self.color else 'ч/б'
        return f'{self.title}, {self.price} р., {self.count} шт., {self.size} кг., {color}'

class Scaner(OfficeEq):

    def __init__(self, title, price, count, size, type_sc):
        super().__init__(title, price, count, size)
        self.type_sc = type_sc

    def __str__(self):
        return f'{self.title}, {self.price} р., {self.count} шт., {self.size} кг., {self.type_sc}'

class Xerox(OfficeEq):

    def __init__(self, title, price, count, size, print_speed):
        super().__init__(title, price, count, size)
        self.print_speed = print_speed

    def __str__(self):
        return f'{self.title}, {self.price} р., {self.count} шт., {self.size} кг., {self.print_speed}'

info_sklad = input("Введите информацию о складе (имя, размер): ").split(',')
sklad = Store(info_sklad[0], int(info_sklad[1]))
while True:
    try:
        info = int(input("Что будем делать: \n1 - Добавить товар\n2 - Забрать товар\n3 - Добавить склад\n4 - информация о складе\n9 - Выход"))
        if info == 9:
            break
        if info == 1:
            while True:
                info = int(input("Чтобы добавить товар введите: \n1 - Принтер\n2 - Сканер\n3 - Ксерокс\n9 - Выход"))
                if info == 9:
                    break
                if info == 1:
                    printer = input("Введите данные принтера в формате название, цена, количество, размер, цветной(1 или 0): ").split(',')
                    sklad.add_to(Printer(printer[0], int(printer[1]), int(printer[2]), int(printer[3]), bool(int(printer[4]))))
                if info == 2:
                    scaner = input("Введите данные сканера в формате название, цена, количество, размер, тип: ").split(',')
                    sklad.add_to(Scaner(scaner[0], int(scaner[1]), int(scaner[2]), int(scaner[3]), scaner[4]))
                if info == 3:
                    xerox = input("Введите данные сканера в формате название, цена, количество, размер, сокрость печати: ").split(',')
                    sklad.add_to(Xerox(xerox[0], int(xerox[1]), int(xerox[2]), int(xerox[3]), xerox[4]))
        if info == 2:
            while True:
                info = int(input("Чтобы забрать товар введите: \n1 - Принтер\n2 - Сканер\n3 - Ксерокс\n9 - Выход"))
                if info == 9:
                    break
                if info == 1:
                    sklad.info()
                    printer = input("Введите данные принтера в формате название, цена, количество, размер, цветной(1 или 0): ").split(',')
                    sklad.give_out(Printer(printer[0], int(printer[1]), int(printer[2]), int(printer[3]), bool(int(printer[4]))))
                if info == 2:
                    sklad.info()
                    scaner = input("Введите данные сканера в формате название, цена, количество, размер, тип: ").split(',')
                    sklad.give_out(Scaner(scaner[0], int(scaner[1]), int(scaner[2]), int(scaner[3]), scaner[4]))
                if info == 3:
                    sklad.info()
                    xerox = input("Введите данные сканера в формате название, цена, количество, размер, сокрость печати: ").split(',')
                    sklad.give_out(Xerox(xerox[0], int(xerox[1]), int(xerox[2]), int(xerox[3]), xerox[4]))
        if info == 4:
            sklad.info()
    except:
        print('Неверный формат ввода')
