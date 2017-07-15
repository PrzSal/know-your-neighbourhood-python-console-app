from Models.location import Location


class CityMunicipality(Location):
    quantity_cm = 0

    def __init__(self, city_municipality, types):
        self.__class__.quantity_cm += 1
        super().__init__(city_municipality, types)

    def __str__(self):
        string = '|  {} | {}             |'.format(__class__.quantity_cm, self.types)
        return string
