from Controller.data_controller import *


def getkey(custom):
    return custom.location, custom.types


def search_location(input_user):
    '''
    Args:
    - input_user (string)
    Funcions search location for user question
    ---------------------------------
    Return:
        None
    '''
    if len(input_user) > 0:
        title_str = CompareLocation()
        find_locations = []

        for row in CompareLocation.all_locations:
            if input_user in row.location:
                find_locations += [row]

        find_locations = sorted(find_locations, key=getkey)
        get_message('Found {} location(s):'.format(len(find_locations)))
        print_search_table(title_str, find_locations)

    else:
        get_message('Wrong lenght word')
