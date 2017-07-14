from Controller.data_controller import *


def three_large_city_sort(list_):
    '''
    Function sort list of object and
    ---------------------------------
    Return:
        None
    '''
    sorted = False
    while not sorted:
        sorted = True

        for step in range(len(list_)-1):
            if len(list_[step][0]) > len(list_[step+1][0]):
                temporary = list_[step+1]
                list_[step+1] = list_[step]
                list_[step] = temporary
                sorted = False
    create_three_city_list(list_)


def create_three_city_list(list_):
    '''
    Function choose three object from sort
    list and send list three city to print table
    module
    ---------------------------------
    Return:
    '''
    title_list = ['location']
    location = []
    for i in range(len(list_)-3, len(list_)):
        location += [list_[i]]
    print_table(location, title_list)
