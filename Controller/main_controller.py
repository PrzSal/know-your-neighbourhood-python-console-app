from Controller.data_controller import *
from Views.main_view import *


def start_main_controller():
    '''
    Main Function in this module

    Return:
        None
    '''
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
            
            three_large_city(County.countys)

        elif choice == '3':
            grade_assignment()

        elif choice == '4':
            check_attendance(Student.students_list)

        elif choice == '5':
            while choice != '0':

                print_menu(['remove_student', 'add_student'])
                choice = get_choice()

                if choice == '1':
                    remove_student()

                elif choice == '2':
                    add_student()
                    print(Student.students_list)
