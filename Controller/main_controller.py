from Controller.data_controller import *
from Views.main_view import *


def start_main_controller():
    '''
    Main Function in this module

    Return:
        None
    '''
    read_file()
    handle_choice()


def handle_choice():
    '''
    Function responsible for moving in menu

    Return:
        None
    '''
    choice = ''
    while choice != '0':
        main_menu = ['List statistics', 'Display 3 cities with longest names',
                     "Display county's name with the largest number of communities",
                     'Display locations, that belong to more than one category',
                     'Advanced search', 'Exit program']

        print_menu(main_menu)
        choice = get_choice()

        if choice == '1':
            list_statistic()

        elif choice == '2':
            three_large_city(City.city_list)

        elif choice == '3':
            county_with_the_largest_communities(NumberOfCommunity.number_community_list)

        elif choice == '4':
            same_locations_in_more_one_category()

        elif choice == '5':
            pass
