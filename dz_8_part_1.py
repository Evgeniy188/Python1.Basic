class MyErr(Exception):
    def __init__(self, text):
        self.text = text


class MyData:
    def __init__(self, s: str):
        try:
            self.day, self.month, self.year = MyData.set_data(s)
            if self.day == None:
                raise MyErr('Неверный формат ввода. Введите в формате d-m-y.')
            a = MyData.check_data(self)
            if a != True:
                self.day, self.month, self.year = None, None, None
                raise a
        except MyErr as err:
            print(err)

    @classmethod
    def set_data(cls, s: str):
        try:
            d, m, y = map(int, s.split(sep='-'))
            return d, m, y
        except:
            return None, None, None

    @staticmethod
    def check_data(obj):
        try:
            if obj.day < 1 or obj.day > 31:
                raise MyErr('Неверно введен день!')
            if obj.month < 1 or obj.month > 12:
                raise MyErr('Неверно введен месяц!')
            if obj.year > 2021:
                raise MyErr('Неверно введен год!')
            return True
        except MyErr as err:
            return err


s1 = '01-05-2021'
s2 = 'asd-sdg-sxcz'
s3 = '0 - 12 - 2022'
s4 = '2 - 13 - 2022'
s5 = '2 - 8 - 2022'

data1 = MyData(s1)
print(data1.day, data1.month, data1.year)

data2 = MyData(s2)
print(data2.day, data2.month, data2.year)

data3 = MyData(s3)
print(data3.day, data3.month, data3.year)

data4 = MyData(s4)
print(data4.day, data4.month, data4.year)

data5 = MyData(s5)
print(data5.day, data5.month, data5.year)
