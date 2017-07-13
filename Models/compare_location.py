class CompareLocation:

    same_location_list = []

    def __init__(self):
        self.location_list = []

    def add_location(self, location, types):
        """
        Atribute:
            location, types
        Collect locations and types for comparison in tupple
        Returns:
            list of tupple
        """
        self.location_list.append((location, types))

    def __eq__(self, location):
        """Less-than comparison."""
        return self.get_perimeter() == location.get_perimeter()

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
        self.location_list = []

    def compare_location(self):
        """
        Compare location for one county and while find same location
        save to list
        Returns:
            list or None
        """
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
