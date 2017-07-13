class Voivodeships:
    voivodeships_list = []
    quantity = 0

    def __init__(self, voivodeships, types, county='po', city_municipality='gm',
                 rural_commune='gw', rural_town='omw',  rural_area='ow', city='m',
                 city_county='mnpp', delegacy='de'):
        Voivodeships.voivodeships_list.append(self)
        self.voivodeships = voivodeships
        self.county = county
        self.city_municipality = city_municipality
        self.rural_commune = rural_commune
        self.rural_town = rural_town
        self.rural_area = rural_area
        self.city = city
        self.city_county = city_county
        self.delegacy = delegacy
        self.types = types
        self.__class__.quantity += 1

    def __str__(self):
        string = '{}, type: {}'.format(Voivodeships.quantity, self.types)
        return string
