from Models.voivodeships import Voivodeships


class County(Voivodeships):
    countys = []
    quantity_c = 0

    def __init__(self, county, types):
        self.__class__.quantity_c += 1
        super().__init__(county, types)
        County.countys.append([county])

    def __str__(self):

        # if __class__.str_quantity < 3:
        string = '{},  type: {}'.format(__class__.quantity_c, self.types)

        return string
