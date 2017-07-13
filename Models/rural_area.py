from Models.voivodeships import Voivodeships


class RuralArea(Voivodeships):
    rural_area_list = []
    rural_area_type = ''
    quantity_ra = 0

    def __init__(self, rural_area, types):
        self.__class__.quantity_ra += 1
        self.__class__.rural_area_type = types
        super().__init__(rural_area, types)
        RuralArea.rural_area_list.append(self)

    def __str__(self):
        string = '|  {} | {}            |'.format(RuralArea.quantity_ra, self.types)
        return string
