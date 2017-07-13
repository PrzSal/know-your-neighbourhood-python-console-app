from Models.voivodeships import Voivodeships


class Delegacy(Voivodeships):
    delegacy_list = []
    delegacy_type = ''
    quantity_d = 0

    def __init__(self, delegacy, types):
        Delegacy.delegacy_list.append(self)
        self.__class__.quantity_d += 1
        self.__class__.delegacy_type = types
        super().__init__(delegacy, types)

    def __str__(self):
        string = '|   {} | {}                |'.format(__class__.quantity_d, self.types)
        return string
