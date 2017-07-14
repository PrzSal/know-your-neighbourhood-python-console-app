class CompareLocation:
    temporary_location_list = []
    same_location_list = []
    all_locations = []

    def __init__(self, location='location', types='types'):
        self.location = location
        self.types = types

    def __str__(self):
        string = '| {}{} | {}{} |'.format(self.location, ' '*(23-len(self.location)),
                                          self.types, ' '*(25-len(self.types)))
        return string

    def __eq__(self, location):
        """Less-than comparison."""
        return self.get_perimeter() == location.get_perimeter()

    def add_location(self):
        """
        Atribute:
            location, types
        Collect locations and types for comparison in tupple
        Returns:
            list of tupple
        """
        __class__.temporary_location_list.append((self.location, self.types))
        __class__.all_locations.append(CompareLocation(self.location, self.types))

    def add_same_location(self):
        """
        Save same locations for all user
        Returns:
            list
        """
        __class__.same_location_list.append(self)

    def remove_list_location(self):
        """
        Data cleaning for new data in county
        Returns:
            empty list
        """
        __class__.temporary_location_list = []

    def compare_location(self):
        """
        Compare location for one county and while find same location
        save to list
        Returns:
            list or None
        """
        try:
            for i in range(len(__class__.temporary_location_list)):
                same_location = __class__.temporary_location_list[i][0]
                type_location = __class__.temporary_location_list[i][1]
                for location in __class__.temporary_location_list:
                    if location[0] == same_location and location[1] != type_location:
                        if location[0] not in __class__.same_location_list:
                            __class__.add_same_location(location[0])

        except IndexError:
            pass
