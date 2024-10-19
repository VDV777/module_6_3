# Необходимо написать 3 класса:
# Horse - класс описывающий лошадь. Объект этого класса обладает следующими атрибутами:
# x_distance = 0 - пройденный путь.
# sound = 'Frrr' - звук, который издаёт лошадь.
# И методами:
# run(self, dx), где dx - изменение дистанции, увеличивает x_distance на dx.
#
# Eagle - класс описывающий орла. Объект этого класса обладает следующими атрибутами:
# y_distance = 0 - высота полёта
# sound = 'I train, eat, sleep, and repeat' - звук, который издаёт орёл (отсылка)
# И методами:
# fly(self, dy) где dy - изменение дистанции, увеличивает y_distance на dy.
#
# Pegasus - класс описывающий пегаса. Наследуется от Horse и Eagle в том же порядке.
# Объект такого класса должен обладать атрибутами классов родителей в порядке наследования.
# Также обладает методами:
# move(self, dx, dy) - где dx и dy изменения дистанции. В этом методе должны запускаться наследованные методы run и fly соответственно.
# get_pos(self) возвращает текущее положение пегаса в виде кортежа - (x_distance, y_distance) в том же порядке.
# voice - который печатает значение унаследованного атрибута sound.

class Horse:

    def __init__(self):
        super().__init__()

        self.x_distance: int = 0
        self.sound: str = 'Frrr'

    def run(self, dx: int):

        self.x_distance += dx


class Eagle:

    def __init__(self):

        self.y_distance: int = 0
        self.sound: str = 'I train, eat, sleep, and repeat'

    def fly(self, dy: int):

        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()

    def move(self, dx: int, dy: int):

        self.run(dx)
        self.fly(dy)

    def get_pos(self) -> tuple:

        return self.x_distance, self.y_distance

    def voice(self) -> None:
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()