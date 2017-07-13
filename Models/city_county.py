from Models.voivodeships import Voivodeships


class CityCounty(Voivodeships):
    city_county_list = []
    number_of_elements = 0
    city_county = ''

    def __init__(self, city_county, types):
        CityCounty.city_county_list.append(self)
        self.__class__.number_of_elements += 1
        self.__class__.city_county = types
        super().__init__(city_county, types)

    def __str__(self):
        string = '|   {} | {} |'.format(__class__.number_of_elements, self.types)
        return string
