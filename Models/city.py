from Models.location import Location


class City(Location):
    city_list = []
    quantity_ci = 0

    def __init__(self, city, types):
        self.__class__.quantity_ci += 1
        super().__init__(city, types)
        City.city_list.append([city])

    def __str__(self):
        string = '|  {} | {}                    |'.format(City.quantity_ci, self.types)
        return string
