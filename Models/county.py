from Models.voivodeships import Voivodeships
from Models.number_of_community import NumberOfCommunity


class County(Voivodeships):
    countys = []
    quantity_c = 0

    def __init__(self, county, types):
        self.__class__.quantity_c += 1
        super().__init__(county, types)
        County.countys.append(county)

    def __str__(self):
        string = '{},  type: {}'.format(self.county, self.types)
        return string
