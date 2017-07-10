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
        mentor_menu = ['Show students', 'Add assignment', 'Grade assignment',
                       'Check attendence', 'Edit_student']
        print_menu(mentor_menu)
        choice = get_choice()

        if choice == '1':
            print_list(append_with_file())

        elif choice == '2':
            add_new_assignment()
            print_list(Assignment.assignments_list)

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
