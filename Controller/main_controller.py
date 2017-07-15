from Controller.data_controller import *
from Controller.search_controller import search_location
from Controller.three_city_controller import three_large_city_sort
from Controller.largest_communities_controller import county_with_the_largest_communities
from Controller.same_locations_controller import same_locations_in_more_one_category


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
                     'Advanced search']

        print_menu(main_menu)
        choice = get_choice()

        if choice == '1':
            list_statistic()

        elif choice == '2':
            three_large_city_sort(City.city_list)

        elif choice == '3':
            county_with_the_largest_communities(NumberOfCommunity.number_community_list)

        elif choice == '4':
            same_locations_in_more_one_category()

        elif choice == '5':
            search_location(get_search())
