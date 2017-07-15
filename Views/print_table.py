def create_list_max_width_col(table):
    '''
    table (list in list)
    Function that create list with max width colummn
    ---------------------------------
    Return:
        List
    '''
    sorted = False
    ammount_of_column = len(table[0])

    max_elem_col = 0
    list_max_elem_col = []
    for i in range(ammount_of_column):
        for j in range(len(table)):
            if max_elem_col < len(table[j][i]):
                max_elem_col = len(table[j][i])
        list_max_elem_col += [max_elem_col]
        max_elem_col = 0
    return list_max_elem_col


def print_insert_row_for_table(list_max_elem_col):
    '''
    Args:
    list_max_elem_col (list)
    Funcions print row between two data row
    ---------------------------------
    Return:
        None
    '''
    sorted = False
    for elem in list_max_elem_col:
        print('|' + '-'*elem + '-'*4, end='')
    print('|')


def print_row_name_column(title_list, list_max_elem_col):
    '''
    Args:
    - tittle_list (list)
    - list_max_elem_col (list)
    Funcions print first row with tittle
    ---------------------------------
    Return:
        None
    '''
    for i in range(len(title_list)):
        print('|  ' + title_list[i] + ' '*(list_max_elem_col[i] - len(title_list[i]) + 2), end='')
    print('|')


def print_content_from_table_in_row(table, list_max_elem_col):
    '''
    Args:
    - table (list in list)
    - list_max_elem_col (list)
    Funcions print data row
    ---------------------------------
    Return:
        None
    '''
    for i in range(1, len(table)):
        print_insert_row_for_table(list_max_elem_col)
        for j in range(len(list_max_elem_col)):
            print('|  ' + str(table[i][j]) + ' '*(list_max_elem_col[j] - len(table[i][j]) + 2), end='')
        print('|')


def print_table(table, title_list):
    '''
    Args:
    - table (list in list)
    - tittle_list (list)
    Funcions print all funcions with row
    ---------------------------------
    Return:
        None
    '''
    table = [title_list] + table

    list_max_elem_col = create_list_max_width_col(table)

    sum_list_max_elem_col = 0
    for elem in list_max_elem_col:
        sum_list_max_elem_col += elem

    print('/' + '-'*(sum_list_max_elem_col + (len(list_max_elem_col))*5 - 1) + '\\')
    print_row_name_column(title_list, list_max_elem_col)
    print_content_from_table_in_row(table, list_max_elem_col)
    print('\\' + '-'*(sum_list_max_elem_col + (len(list_max_elem_col))*5 - 1) + '/')
