class House():
    def __init__(self,rayon, street, number):
        self.__rayon = rayon
        self.__street = street
        self.__number = number
    @property
    def rayon(self):
        return self.__rayon
    @rayon.setter
    def rayon(self, rayon):
        if isinstance(rayon, str):
            self.__rayon = rayon

    @property
    def street(self):
        return self.__street

    @street.setter
    def street(self, street):
        if isinstance(street, str):
            self.__rayostreet = street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if isinstance(number, int):
            self.__number = number

    def build(self):
        print('Дом находится в районе:' + self.__rayon + 'на улице:' + self.__strret + 'под номером' + self.__number)
if __name__ == '__main__':
    House1 = House("Советский", "Панфилова", 5)
    House1.build()
    print(f'Дом находится в районе: {House1.rayon()}, на улице: {House1.street()}), под номером {House1.number()}')
    House1.rayon = 'Центральный'
    print('После изменении имени:')
    print(f'Дом находится в районе: {House1.rayon()}, на улице: {House1.street()}), под номером {House1.number()}')





