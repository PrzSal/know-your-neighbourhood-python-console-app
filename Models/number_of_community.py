class NumberOfCommunity:
    number_community = 0
    number_community_list = []

    def __init__(self, county='po'):
        self.county = county
        self.__class__.number_community += 1

    def add_county(self):
        __class__.number_community_list.append(self)

    def add_number(self):
        __class__.number_community_list.append(self)
