from Models.location import Location


class Voivodeships(Location):
    quantity_v = 0

    def __init__(self, delegacy, types):
        self.__class__.quantity_v += 1
        super().__init__(delegacy, types)

    def __str__(self):
        string = '|   {} | {}               |'.format(Voivodeships.quantity_v, self.types)
        return string
