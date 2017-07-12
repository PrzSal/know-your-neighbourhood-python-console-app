import csv
from Models.county import County
from Models.voivodeships import Voivodeships
from Models.city_county import CityCounty
from Models.city_municipality import CityMunicipality
from Models.rural_commune import RuralCommune
from Models.number_of_community import NumberOfCommunity
from Models.rural_town import RuralTown
from Models.rural_area import RuralArea
from Models.compare_location import CompareLocation
from Views.main_view import *
from Views.print_table import *


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
        student = ''
        reader = csv.reader(f, delimiter=',')
        compare_location = CompareLocation()
        for row in reader:
            if 'województwo' in row:
                print_list(Voivodeships(voivodeships=row[4], types=row[5]))
            elif 'powiat' in row or 'miasto na prawach powiatu' in row:
                compare_location.remove_list_location()
                NumberOfCommunity.add_county_and_number(student, NumberOfCommunity.number_community)
                if row[4] not in NumberOfCommunity.number_community_list:
                    student = row[4]
                compare_location.add_location(row[4], row[5])
                print_list(County(county=row[4], types=row[5]))
                NumberOfCommunity.number_community = 0
            elif 'gmina miejska' in row:
                print_list(CityMunicipality(city_municipality=row[4], types=row[5]))
                NumberOfCommunity()
                compare_location.add_location(row[4], row[5])
            elif 'gmina wiejska' in row:
                print_list(RuralCommune(rural_commune=row[4], types=row[5]))
                NumberOfCommunity()
                compare_location.add_location(row[4], row[5])
            elif 'gmina miejsko-wiejska' in row:
                print_list(RuralTown(rural_town=row[4], types=row[5]))
                NumberOfCommunity()
                compare_location.add_location(row[4], row[5])
            elif 'obszar wiejski' in row:
                print_list(RuralArea(rural_area=row[4], types=row[5]))
                NumberOfCommunity()
                compare_location.add_location(row[4], row[5])
            elif 'miasto na prawach powiatu' == row[5]:
                print_list(CityCounty(row[4], row[5]))
                NumberOfCommunity()
                compare_location.add_location(row[4], row[5])
            compare_location.compare_location()


def three_large_city(list_):
    sorted = False
    while not sorted:
        sorted = True
        for step in range(len(list_)-1):
            if len(list_[step][0]) > len(list_[step+1][0]):
                temporary = list_[step+1]
                list_[step+1] = list_[step]
                list_[step] = temporary
                sorted = False
    title_list = ['location']
    location = []
    for i in range(len(list_)-3, len(list_)):
        location += [list_[i]]
    print_table(location, title_list)


def county_with_the_largest_communities(list_):
    sorted = False
    while not sorted:
        sorted = True
        for step in range(len(list_)-1):
            if int(list_[step][1]) > int(list_[step+1][1]):
                temporary = list_[step+1]
                list_[step+1] = list_[step]
                list_[step] = temporary
                sorted = False
    title_list = ['location', 'type']
    print_table(list_[-1:], title_list)

def same_locations_in_more_one_category():
    print_compare_list(CompareLocation.same_location_list)
