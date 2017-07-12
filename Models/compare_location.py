class CompareLocation:

    same_location_list = []

    def __init__(self):
        self.location_list = []

    def add_location(self, location, types):
        self.location_list.append((location, types))

    def __eq__(self, other):
        """Less-than comparison."""
        return self.get_perimeter() == other.get_perimeter()

    def add_same_location(self):
        __class__.same_location_list.append(self)

    def remove_list_location(self):
        self.location_list = []

    def compare_location(self):
        try:
            for i in range(len(self.location_list)):
                same_location = self.location_list[i][0]
                type_location = self.location_list[i][1]

                for location in self.location_list:
                    if location[0] == same_location and location[1] != type_location:
                        if location[0] not in __class__.same_location_list:
                            __class__.add_same_location(location[0])

        except IndexError:
            pass
