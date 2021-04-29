class Worker:
    def __init__(self, name, surname, wage, bonus, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


pos1 = Position('Jo', 'Black', 750.3, 53.1)
pos2 = Position('Mike', 'White', 555, 32)
print(pos1.name, pos1.surname, pos1.position, pos1._income)
print(pos2.name, pos2.surname, pos2.position, pos2._income)
print(pos1.get_full_name(), pos2.get_full_name(), sep='\n')
print(pos1.get_total_income(), pos2.get_total_income(), sep='\n')
