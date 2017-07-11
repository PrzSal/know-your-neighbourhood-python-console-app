class Voivodeships:
    voivodeships_list = []
    county_list = []
    quantity = 0

    def __init__(self, voivodeships, types, county='po',
                 city_municipality='cm', rural_commune='gw',):
        Voivodeships.voivodeships_list.append(self)
        self.voivodeships = voivodeships
        self.county = county
        self.city_municipality = city_municipality
        self.rural_commune = rural_commune
        self.types = types
        self.__class__.quantity += 1

    def __str__(self):
        string = '{}, type: {}'.format(Voivodeships.quantity, self.types)
        return string
