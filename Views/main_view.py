def get_choice():
    '''
    Function that ask user about his choise(which option did he take in menu)
    ---------------------------------
    Return:
        string with your input
    '''
    return input("Your choice : ")


def get_search():
    '''
    Function that ask user about his search
    ---------------------------------
    Return:
        string with your input
    '''
    return input("Searching for: ")


def print_statistic_list(list_):
    '''
    Atribute:
        list of object
    Function that create table to statistics option
    ---------------------------------
    Return:
        None
    '''

    if list_:
        types_list = []
        try:
            print("/---------------------------------\\")
            print("|       {}               |".format(list_[0].voivodeships))
            for i in range(len(list_)):
                if list_[i].types not in types_list:
                    print("|---------------------------------|")
                    print(list_[i])
                    types_list.append(list_[i].types)
            print("\---------------------------------/")
        except TypeError:
            print('error', [i])
    else:
        print('Empty List')


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
