class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go - Go - Go !', self.name)

    def stop(self):
        print('STOP!!!', self.name)

    def turn(self, direciton):
        print('Turn to ' + direciton, self.name)

    def show_speed(self):
        print('Speed your car =', self.speed, self.name)


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print('Your speed is greater', self.name)
        else:
            super(TownCar, self).show_speed()


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print('Your speed is greater!!!', self.name)
        else:
            super(WorkCar, self).show_speed()


class SportCar(Car):
    def __init__(self, speed, color, name, team_name, sponsor):
        super(SportCar, self).__init__(speed, color, name, False)
        self.team_name = team_name
        self.sponsor = sponsor


class PoliceCar(Car):
    def __init__(self, speed, color, name, police_station):
        super(PoliceCar, self).__init__(speed, color, name, True)
        self.police_station = police_station


town_car1 = TownCar(70, 'black', 'towncar1')
town_car2 = TownCar(50, 'white', 'towncar2')
work_car1 = WorkCar(50, 'black', 'workcar1')
work_car2 = WorkCar(30, 'white', 'workcar2')
sport_car = SportCar(400, 'red', 'sportcar', 'F1', 'BMW')
police_car = PoliceCar(90, 'blue', 'policecar', 'Moscow')

print(town_car1.name, town_car1.color, town_car1.speed, town_car1.is_police, sep=' - ')
print(town_car2.name, town_car2.color, town_car2.speed, town_car2.is_police, sep=' - ')
print(work_car1.name, work_car1.color, work_car1.speed, work_car1.is_police, sep=' - ')
print(work_car2.name, work_car2.color, work_car2.speed, work_car2.is_police, sep=' - ')
print(sport_car.name, sport_car.team_name, sport_car.sponsor, sport_car.color, sport_car.speed, sport_car.is_police,
      sep=' - ')
print(sport_car.name, police_car.police_station, police_car.color, police_car.speed, police_car.is_police, sep=' - ')
sport_car.go()
sport_car.show_speed()
sport_car.turn('right')
sport_car.stop()
police_car.go()
police_car.show_speed()
police_car.turn('left')
police_car.stop()
town_car1.show_speed()
town_car2.show_speed()
work_car1.show_speed()
work_car2.show_speed()
