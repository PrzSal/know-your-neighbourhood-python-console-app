class NumberOfCommunity:
    number_community = 0
    number_community_list = []

    def __init__(self, county='po'):
        self.county = county
        self.__class__.number_community += 1

    @staticmethod
    def add_county_and_number(county, number):
        """
        Atribute:
            county, number
        Add to list name county and how much communities in this county
        Returns:
            list of tupple
        """
        __class__.number_community_list.append((county, str(number)))

    def __gt__(self, other):
        return self.__class__.number_community
