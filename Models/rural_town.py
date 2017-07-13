from Models.voivodeships import Voivodeships


class RuralTown(Voivodeships):
    rural_town_list = []
    rural_town_type = ''
    quantity_rt = 0

    def __init__(self, rural_town, types):
        RuralTown.rural_town_list.append(self)
        self.__class__.quantity_rt += 1
        self.__class__.rural_town_type = types
        super().__init__(rural_town, types)

    def __str__(self):
        string = '|  {} | {}     |'.format(RuralTown.quantity_rt, self.types)
        return string
