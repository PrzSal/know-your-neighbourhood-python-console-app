class Voivodeships:
    voivodeships_list = []

    def __init__(self, county='s', voivodeships='s', types='s'):
        Voivodeships.voivodeships_list.append(self)
        self.voivodeships = voivodeships
        self.county = county
        self.types = types

    def __str__(self):
        string = 'wojewdztwo: {}, type: {}'.format(self.voivodeships, self.types)
        return string
