from Controller.data_controller import *


def same_locations_in_more_one_category():
    '''
    Function that read object with same
    location and send list to print table
    module
    ---------------------------------
    Return:
        None
    '''
    title_list = ['location']
    locations = []
    for row in CompareLocation.same_location_list:
        locations += [[row]]

    locations = sorted(locations)
    print_table(locations, title_list)
