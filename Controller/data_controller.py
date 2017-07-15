import csv
from Models.location import Location
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
                Voivodeships(row[4], row[5])

            elif 'powiat' in row:
                compare_location.remove_list_location()
                NumberOfCommunity.add_county_and_number(county_temporary, NumberOfCommunity.number_community)

                if row[4] not in NumberOfCommunity.number_community_list:
                    county_temporary = row[4]

                CompareLocation(row[4], row[5]).add_location()
                County(row[4], row[5])
                NumberOfCommunity.number_community = 0

            elif 'gmina miejska' in row:
                CityMunicipality(row[4], row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'gmina wiejska' in row:
                RuralCommune(row[4], row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'gmina miejsko-wiejska' in row:
                RuralTown(rural_town=row[4], types=row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'obszar wiejski' in row:
                RuralArea(row[4], row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'miasto' in row:
                City(row[4], row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'miasto na prawach powiatu' in row:
                CityCounty(row[4], row[5])
                NumberOfCommunity()
                CompareLocation(row[4], row[5]).add_location()

            elif 'delegatura' in row:
                Delegacy(row[4], row[5])
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
    print_statistic_list(Location.location_list)
