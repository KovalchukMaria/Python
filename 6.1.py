class TrafficLight:
    __color = 'red'

    def running(self, __color):
        '''вывод стартового цвета'''
        print(__color)
        '''импорт задержки кода'''
        import time
        time.sleep(7)
        tim = 0
        '''почередная замена значений'''
        while tim < 10:
            if __color == 'red':
                __color = 'yellow'
                print(__color)
                time.sleep(2)
                tim += 1

            if __color == 'yellow':
                __color = 'green'
                print(__color)
                time.sleep(8)
                tim += 1

            if __color == 'green':
                __color = 'red'
                print(__color)
                time.sleep(7)
                tim += 1
        else:
            print('программа завершена. выведено 4 последовательных значения')
            return __color


t = TrafficLight()
print(t.running('red'))
