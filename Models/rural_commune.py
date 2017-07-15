from Models.location import Location


class RuralCommune(Location):
    quantity_rc = 0

    def __init__(self, rural_commune, types):
        self.__class__.quantity_rc += 1
        super().__init__(rural_commune, types)

    def __str__(self):
        string = '| {} | {}             |'.format(__class__.quantity_rc, self.types)
        return string
