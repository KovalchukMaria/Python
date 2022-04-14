class Road:
    def __int__(self, _length, _width):
        pass
    def mass(self, _length, _width, mas_1m2, thickness_cm):
        m = _length * _width * mas_1m2 * thickness_cm
        return m


r = Road()
print(f'масса требуемого асфальта - {r.mass(20, 5000, 25, 5)}')

