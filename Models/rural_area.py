from Models.location import Location


class RuralArea(Location):
    quantity_ra = 0

    def __init__(self, rural_area, types):
        self.__class__.quantity_ra += 1
        super().__init__(rural_area, types)

    def __str__(self):
        string = '|  {} | {}            |'.format(RuralArea.quantity_ra, self.types)
        return string
