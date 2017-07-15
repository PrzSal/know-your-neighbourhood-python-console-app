class Location:
    location_list = []

    def __init__(self, location, types):

        Location.location_list.append(self)
        self.location = location
        self.types = types
