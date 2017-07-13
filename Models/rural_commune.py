from Models.voivodeships import Voivodeships


class RuralCommune(Voivodeships):
    rural_commune_list = []
    rural_commune_type = ''
    quantity_rc = 0
    str_quantity = 0

    def __init__(self, rural_commune, types):
        RuralCommune.rural_commune_list.append(self)
        self.__class__.quantity_rc += 1
        self.__class__.rural_commune_type = types
        super().__init__(rural_commune, types)

    def __str__(self):
        string = '| {} | {}             |'.format(__class__.quantity_rc, self.types)
        return string