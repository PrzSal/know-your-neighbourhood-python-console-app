import csv
from Models.voivodeships import Voivodeships
from Models.county import County
from Models.city_county import CityCounty
from Models.city_municipality import CityMunicipality
from Models.rural_commune import RuralCommune
from Models.number_of_community import NumberOfCommunity
from Models.rural_town import RuralTown
from Models.rural_area import RuralArea
from Models.city import City
from Models.delegacy import Delegacy
from Models.compare_location import CompareLocation
from Views.main_view import *
from Views.print_table import *


def read_file():
    '''
    Function that read data from csv file
    and assigns to data to the appropriate class
    ---------------------------------
    Return:
        None
    '''
    with open('malopolska.csv') as file_reader:
        county_temporary = ''
        reader = csv.reader(file_reader, delimiter=',')
        compare_location = CompareLocation()

        for row in reader:
            if 'województwo' in row:
                Voivodeships(voivodeships=row[4], types=row[5])

            elif 'powiat' in row:
                compare_location.remove_list_location()
                NumberOfCommunity.add_county_and_number(county_temporary, NumberOfCommunity.number_community)

                if row[4] not in NumberOfCommunity.number_community_list:
                    county_temporary = row[4]

                CompareLocation(row[4], row[5]).add_location()
                County(county=row[4], types=row[5])
                NumberOfCommunity.number_community = 0

            elif 'gmina miejska' in row:
                CityMunicipality(city_municipality=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'gmina wiejska' in row:
                RuralCommune(rural_commune=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'gmina miejsko-wiejska' in row:
                RuralTown(rural_town=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'obszar wiejski' in row:
                RuralArea(rural_area=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'miasto' in row:
                City(city=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'miasto na prawach powiatu' in row:
                CityCounty(city_county=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'delegatura' in row:
                Delegacy(delegacy=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            compare_location.compare_location()


def list_statistic():
    '''
    Function that send list with object
    to view module to display object
    ---------------------------------
    Return:
        None
    '''
    print_statistic_list(Voivodeships.voivodeships_list)


def three_large_city(list_):
    '''
    Function sort list of object and
    send list three city to print table
    module
    ---------------------------------
    Return:
        None
    '''
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
    '''
    Function that read object with same
    location and send list to print table
    module
    ---------------------------------
    Return:
        None
    '''
    title_list = ['location']
    location = []
    for row in CompareLocation.same_location_list:
        location += [[row]]
    print_table(location, title_list)


def search_location(input_user):
    title_list = 'Searching for: ' + input_user
    find_locations = []

    for row in CompareLocation.all_locations:
        if input_user in row.location:
            find_locations += [row]

    print_search_table(title_list, find_locations)
