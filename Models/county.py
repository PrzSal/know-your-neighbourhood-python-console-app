from Models.voivodeships import Voivodeships


class County(Voivodeships):
    countys = []

    def __init__(self, county='s', voivodeships='s', types='s'):
        County.countys.append(self)
        super().__init__(county, voivodeships, types)

    def __str__(self):
        string = 'name conty: {},  type: {}'.format(self.county, self.types)
        return string
