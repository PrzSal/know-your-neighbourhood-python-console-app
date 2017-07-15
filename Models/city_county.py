from Models.location import Location


class CityCounty(Location):
    quantity_cc = 0

    def __init__(self, city_county, types):
        self.__class__.quantity_cc += 1
        super().__init__(city_county, types)

    def __str__(self):
        string = '|   {} | {} |'.format(__class__.quantity_cc, self.types)
        return string
