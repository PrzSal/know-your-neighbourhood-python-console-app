from Models.county import County


class CityMunicipality(County):
    city_municipality_list = []
    quantity_cm = 0

    def __init__(self, city_municipality, types):
        CityMunicipality.city_municipality_list.append(self)
        self.__class__.quantity_cm += 1
        super().__init__(city_municipality, types)


    def __str__(self):
        string = '{},  type: {}'.format(CityMunicipality.quantity_cm, self.types)
        return string
