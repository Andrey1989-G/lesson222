# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    def __init__(self, position_units: dict, field: dict, way: str, x_coord: float, y_coord: float, speed=1):
        self.position_units = position_units  # example {"x_coord": float, "y_coord": float}
        self.field = field  # example field = {x_start: 0, y_start: 0, x_finite: 10, y_finite: 10}
        # надо бы сделать проверку на вхождение в игровое поле x и y
        self.way = way
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.speed = speed

    def _way(self):
        if self.way == 'crawl':
            self.speed *= 0.5
        elif self.way == 'fly':
            self.speed *= 1.2

    def result(self, direction):
        if direction == 'UP':
            new_y = self.y_coord + self.speed
            new_x = self.x_coord
        elif direction == 'DOWN':
            new_y = self.y_coord - self.speed
            new_x = self.x_coord
        elif direction == 'LEFT':
            new_y = self.y_coord
            new_x = self.x_coord - self.speed
        elif direction == 'RIGTH':
            new_y = self.y_coord
            new_x = self.x_coord + self.speed
        self.position_units = {"x_coord": new_x, "y_coord": new_y}
        return self.position_units

# class Unit:
#     def move(self, field, x_coord, y_coord, direction, is_fly, crawl, speed = 1):
#
#         if is_fly and crawl:
#             raise ValueError('Рожденный ползать летать не должен!')
#
#         if is_fly:
#             speed *= 1.2
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#         if crawl:
#             speed *= 0.5
#             if direction == 'UP':
#                 new_y = y_coord + speed
#                 new_x = x_coord
#             elif direction == 'DOWN':
#                 new_y = y_coord - speed
#                 new_x = x_coord
#             elif direction == 'LEFT':
#                 new_y = y_coord
#                 new_x = x_coord - speed
#             elif direction == 'RIGTH':
#                 new_y = y_coord
#                 new_x = x_coord + speed
#
#             field.set_unit(x=new_x, y=new_y, unit=self)

#     ...
