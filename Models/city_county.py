class CityCounty:
    city_county_list = []
    number_of_elements = 0

    def __init__(self, city_county, types):
        self.city_county = city_county
        self.types = types
        __class__.city_county_list.append(self)
        self.__class__.number_of_elements += 1
    def __str__(self):
        string = '{} : name city conty: {},  type: {}'.format(CityCounty.number_of_elements, self.city_county, self.types)
        return string
