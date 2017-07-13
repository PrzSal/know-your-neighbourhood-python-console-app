from Models.voivodeships import Voivodeships


class City(Voivodeships):
    city_list = []
    city_type = ''
    quantity_c = 0

    def __init__(self, city, types):
        self.__class__.quantity_c += 1
        self.__class__.city_type = types
        super().__init__(city, types)
        City.city_list.append([city])

    def __str__(self):
        string = '|  {} | {}                    |'.format(City.quantity_c, self.types)
        return string
