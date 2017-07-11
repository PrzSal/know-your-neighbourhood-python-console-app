import csv
from Models.county import County
from Models.voivodeships import Voivodeships
from Models.city_county import CityCounty
from Models.city_municipality import CityMunicipality
from Models.rural_commune import RuralCommune
from Models. number_of_community import NumberOfCommunity
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


def list_statistic():
    # csv_row = []
    # for line in open('malopolska.csv'):
    #     csv_row += [line.split(',')]
    with open('malopolska.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if 'województwo' in row:
                print_list(Voivodeships(voivodeships=row[4], types=row[5]))
            elif 'powiat' in row or 'miasto na prawach powiatu' in row:
                if row[4] not in NumberOfCommunity.number_community_list:
                    NumberOfCommunity.add_number(NumberOfCommunity.number_community)
                NumberOfCommunity.add_county(row[4])
                print_list(County(county=row[4], types=row[5]))
                NumberOfCommunity.number_community = 0
            elif 'gmina miejska' in row:
                print_list(CityMunicipality(city_municipality=row[4], types=row[5]))
                NumberOfCommunity()
            elif 'gmina wiejska' in row:
                print_list(RuralCommune(rural_commune=row[4], types=row[5]))
                NumberOfCommunity()
            elif 'miasto na prawach powiatu' == row[5]:
                print_list(CityCounty(row[4], row[5]))
                NumberOfCommunity()
        print_list(NumberOfCommunity.number_community_list)


def three_large_city(list_):
    # with open('malopolska.csv') as f:
    #     reader = csv.reader(f, delimiter=',')
    #     for row in reader:
    #         if 'powiat' in row or 'miasto na prawach powiatu' in row:
    #             County(county=row[4], types=row[5])

        #print_3_city(County.countys)
    sorted = False
    while not sorted:
        sorted = True
        for step in range(len(list_)-1):
            if len(list_[step]) > len(list_[step+1]):
                temporary = list_[step+1]
                list_[step+1] = list_[step]
                list_[step] = temporary
                sorted = False
    print_3_city(list_)
