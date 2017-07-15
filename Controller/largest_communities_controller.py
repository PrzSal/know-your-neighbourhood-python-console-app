from Controller.data_controller import *


def county_with_the_largest_communities(list_):
    '''
    Args:
    - list_ (list in list)
    Funcions choose largest community count
    ---------------------------------
    Return:
        None
    '''
    sorted = False
    while not sorted:
        sorted = True

        for step in range(len(list_)-1):
            if int(list_[step][1]) > int(list_[step+1][1]):
                temporary = list_[step+1]
                list_[step+1] = list_[step]
                list_[step] = temporary
                sorted = False

    title_list = ['location', 'type']
    print_table(list_[-1:], title_list)
