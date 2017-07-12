class CompareLocation:

    same_location_list = []

    def __init_(self, location, types):
        self.location_list = []
        self.location = location
        self.types = types
        self.location_list.append(self)

    def __eq__(self, other):
        """Less-than comparison."""
        return self.get_perimeter() == other.get_perimeter()

    def add_same_location(self):
        County.same_location_list.append((self))

    def compare_Location(self):
        same_location = self.location_list[0]
        for location in self.location_list:
            if location == same_location:
                add_same_location(self)
