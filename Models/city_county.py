class CityCounty:
    city_county_list = []

    def __init__(self, city_county, types):
        self.city_county = city_county
        self.types = types
        CityCounty.city_county_list.append(self)

    def __str__(self):
        string = 'name city conty: {},  type: {}'.format(self.city_county, self.types)
        return string
