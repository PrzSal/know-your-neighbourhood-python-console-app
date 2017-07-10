from Controller.main_controller import *
from Views.main_view import *


def main():

    choose_codecooler()


def choose_codecooler():
    ''' Main loop responsible for work of
    whole program
    '''
    choose = ""

    while choose != "0":

        print_menu(["menager", "administration employee", "mentor", "student"])

        choose = get_input()
        if choose == "1":
            start_main_controller()


if __name__ == '__main__':
    main()
