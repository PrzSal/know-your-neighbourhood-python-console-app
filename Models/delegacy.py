from Models.location import Location


class Delegacy(Location):
    quantity_d = 0

    def __init__(self, delegacy, types):
        self.__class__.quantity_d += 1
        super().__init__(delegacy, types)

    def __str__(self):
        string = '|   {} | {}                |'.format(__class__.quantity_d, self.types)
        return string
