def print_menu(menu_list):
    '''
    Arg:
    menu_list (list)
    Function that take menu options from a file, and print it on the screen.
    ---------------------------------
    Return:
        It prints menu options
    '''
    print('What would you like to do:')
    for options in range(0, len(menu_list)):
        print("(".rjust(6), options + 1, ")", (menu_list[options]))
    print("( 0 )".rjust(10) + " Exit")


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


def get_message(contents):
    '''
    Function that print message user
    ---------------------------------
    Return:
    print message
    '''
    print(contents)


def print_statistic_list(list_):
    '''
    Atribute:
    list of object (list)
    Function that create table to statistics option
    ---------------------------------
    Return:
        None
    '''

    if list_:
        types_list = []
        try:
            print("/---------------------------------\\")
            print("|       {}               |".format(list_[0].location))
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


def print_search_table(tittle_str, list_search):
    '''
    Args:
    - tittle_str (str)
    - list_search (list)
    Funcions print first and between row
    ---------------------------------
    Return:
        None
    '''
    if list_search:
        print("/-----------------------------------------------------\\")
        print(tittle_str)
        for location in list_search:
            print("|-----------------------------------------------------|")
            print(location)
        print("\-----------------------------------------------------/")

    else:
        print('No result to views')
