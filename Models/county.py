from Models.location import Location


class County(Location):
    quantity_c = 0

    def __init__(self, county, types):
        self.__class__.quantity_c += 1
        super().__init__(countiy, types)

    def __str__(self):
        string = '|  {} | {}                    |'.format(__class__.quantity_c, self.types)
        return string
