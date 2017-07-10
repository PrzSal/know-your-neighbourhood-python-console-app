class Voivodeships:
    voivodeships_list = []

    def __init__(self, voivodeships, types):
        Voivodeships.voivodeships_list.append(self)
        self.voivodeships = voivodeships
        self.types = types

    def __str__(self):
        string = 'wojewdztwo: {}, type: {}'.format(self.voivodeships, self.types)
        return string
