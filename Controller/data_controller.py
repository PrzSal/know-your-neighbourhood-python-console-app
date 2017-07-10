import csv
from Models.county import County
from Models.voivodeships import Voivodeships
from Models.city_county import CityCounty
from Views.main_view import *


def write_to_file(file_name, parameter, list_to_write):
    '''
    Function that save data to csv file
    ---------------------------------
    Return:
        None
    '''
    with open(file_name, 'w') as write_file:
        writer = csv.writer(write_file, delimiter='|')
        for row in list_to_write:
            writer.writerow(row)


def write_person_to_file(name, surname, login, password):
    '''
    Function that could save data to csv file in the future.
    ---------------------------------
    Return:
        None
    '''
    pass


def append_with_file():
    # csv_row = []
    # for line in open('malopolska.csv'):
    #     csv_row += [line.split(',')]
    with open('malopolska.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if 'województwo' in row:
                print_list(Voivodeships(voivodeships=row[4], types=row[5]))
            if 'powiat' in row:
                print_list(County(county=row[4], types=row[5]))
            if 'miasto na prawach powiatu' == row[5]:
                print_list(CityCounty(row[4], row[5]))
