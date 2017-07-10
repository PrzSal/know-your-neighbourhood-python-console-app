class County:
    countys = []

    def __init__(self, county, types):
        County.countys.append(self)
        self.county = county
        self.types = types

    def __str__(self):
        string = 'name conty: {},  type: {}'.format(self.county, self.types)
        return string
