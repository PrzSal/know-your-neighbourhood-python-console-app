import csv


def get_choice():
    '''
    Function that ask user about his choise(which option did he take in menu)
    ---------------------------------
    Return:
        string with your input
    '''
    return input("Your choice : ")


def get_input():
    '''
    Function that ask user about his choise(which option did he take in menu)
    ---------------------------------
    Return:
        string with your input
    '''
    return input("Your choice : ")


def print_list(list_):
    '''
    Function that print every element in list_
    ---------------------------------
    Return:
        None
    '''
    if list_:
    #    for element in list_:
        print("--------------------")
        print(list_)
        print("--------------------")
    else:
        print('Empty')


def print_3_city(list_):
    '''
    Function that print every element in list_
    ---------------------------------
    Return:
        None
    '''
    if list_:
        for step in range(len(list_)-3, len(list_)):
            print("--------------------")
            print(list_[step])
            print("--------------------")
    else:
        print('Empty')


def print_compare_list(list_):
    if list_:
        types_list = []
        try:
            for i in range(len(list_)):
                if list_[i].types not in types_list:
                    print("|---------------------------------|")
                    print(list_[i])
                    types_list.append(list_[i].types)
            print("\---------------------------------/")
        except TypeError:
            print('eerror', [i])
    else:
        print('Empty')


def print_menu(menu_list):
    '''
    Function that take menu options from a file, and print it on the screen.
    ---------------------------------
    Return:
        It prints menu options
    '''
    print('What would you like to do:')
    for options in range(0, len(menu_list)):
        print("(".rjust(6), options + 1, ")", (menu_list[options]))
    print("( 0 )".rjust(10) + " Exit")
