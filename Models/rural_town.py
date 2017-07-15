from Models.location import Location


class RuralTown(Location):
    quantity_rt = 0

    def __init__(self, rural_town, types):
        self.__class__.quantity_rt += 1
        super().__init__(rural_town, types)

    def __str__(self):
        string = '|  {} | {}     |'.format(RuralTown.quantity_rt, self.types)
        return string
