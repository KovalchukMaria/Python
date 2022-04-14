class Car:
    '''создание атрибутов'''

    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        is_police = True

    '''создание методов'''

    def go(self):
        print(f'Автомобиль {self.name} поехал')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость автомобиля {self.name} - {self.speed}')


'''создание дочерних классов'''


class TownCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости у автомобиля {self.name}')
        else:
            print(f'Скорость автомобиля {self.name} - {self.speed}')


class SportCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости у автомобиля {self.name}')
        else:
            print(f'Скорость автомобиля {self.name} - {self.speed}')


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)


t = TownCar('volvo', 'red', 70, True)
t.go()
t.show_speed()
s = SportCar('chevrolet', 'yellow', 140, True)
s.turn('направо')
s.show_speed()
w = WorkCar('opel', 'black', 35, True)
w.turn('налево')
w.show_speed()
p = PoliceCar('ваз', 'yellow-green', 30, False)
p.stop()
p.show_speed()
