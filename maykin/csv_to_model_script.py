import requests, re
from django.db import IntegrityError
import os
import django
from ast import literal_eval as make_tuple
import threading

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "maykin.settings")
django.setup()
''' ignoring pylance warning as it works fine on runtime '''
from maykinapp.models import Hotel,City

# following errors upon removing django.setup()
#raise AppRegistryNotReady("Apps aren't loaded yet.")
#django.core.exceptions.AppRegistryNotReady: Apps aren't loaded yet.



def fetch_cities():
    url = 'http://rachel.maykinmedia.nl/djangocase/city.csv'
    response = requests.get(url, auth=('python-demo', 'claw30_bumps'))

    lines = response.text.splitlines()
    city_list = []
    for line in lines:
        city = line.split(";")
        city_list.append((city[0].strip('""'),city[1].strip('""')))
    return city_list


def fetch_hotels():
    url = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
    response = requests.get(url, auth=('python-demo', 'claw30_bumps'))
    
    lines = response.text.splitlines()
    hotel_list = []
    for line in lines:
        hotel = line.split(";")
        hotel_list.append((hotel[0].strip('""'),hotel[1].strip('""'),hotel[2].strip('""')))

    return hotel_list


# fetch_cities()
# fetch_hotels()

""" we will check if the city falls in valid name using regexp """
def validate_cityname(name):
    if re.match("^([a-zA-Z\u0080-\u024F]+(?:. |-| |'))*[a-zA-Z\u0080-\u024F]*$",name):
        return True
    else:
        return False

# print(validate_cityname('Berlijn'))


""" city name check else delete from cities list such as extra random words or symbols """
def validate_city_hotels():
    cities = fetch_cities()
    for city in range(len(cities)):
        if validate_cityname(cities[city][1])==False:
            del cities[city]

    hotels = fetch_hotels()
    # print(len(hotels))    
    city_codes = []
    for city_code in cities:
        city_codes.append(city_code[0])

    """ check if the hotel is in a valid city else remove the hotel from list """
    for hotel in range(len(hotels)):
        if hotels[hotel][0] in city_codes==False:
            # print("removing hotel: ")
            # print(hotels[hotel])
            del hotels[hotel]

    """ we have not added check for hotel name as it can be number and in any language, may be checked with some online registery"""
    return hotels, cities

# validate_city_hotels()
""" check new city list against db saved cities for duplicates """
def get_unique_cities(cities):
    duplicate_cities = []
    db_cities = City.objects.all().values_list('city_code','city_name')
    for count in range(len(cities)):
        if cities[count] in db_cities:
            duplicate_cities.append(cities[count])

    cities = list(set(cities)-set(duplicate_cities))
    return cities


""" check for duplicates against database """
def get_unique_hotels(hotels):
    """ we will get the all hotels  from db as its a bad practice to hit db while saving  """   
    db_hotels = Hotel.objects.all().values_list('hotel_name')
    m_hotels =[]
    """ making hotel name as tuple so that we can make them sets and manipulate easily """
    for counter in range(len(hotels)):
        var  = "(\""+str(hotels[counter][2])+"\","+")"
        var = make_tuple(str(var))
        m_hotels.append(var)

    """ checking duplicate hotels against database and then we only have unique hotels """
    duplicate_hotels = []
    counter = 0

    duplicate_hotels = set(db_hotels).intersection(set(m_hotels))
    m_hotels = set(m_hotels)
    unique_hotels = m_hotels.difference(duplicate_hotels)
    return unique_hotels
    

""" function to save unique cities into the database """
def save_cities_to_db(cities):
    """ finally we will save the cities and hotels into the database """
    for city_count in range(len(cities)):
        city_table = City(city_code=cities[city_count][0],city_name=cities[city_count][1])
        """if model throw any integrity error we want to handle it gracefully"""
        try:
            city_table.save()
        except IntegrityError as e:
            print("Error while saving the city.")
            print(e)


""" function to save unique hotels into the database """
def save_hotels_to_db(unique_hotels):
    """ finally we will save the unique hotels into the database """
    for hotel_count in range(len(unique_hotels)):
        """there can be better approach for handling this but due to time limitation I did it like this """
        city_object = City.objects.get(city_code=unique_hotels[hotel_count][0])
        hotel_table = Hotel(city=city_object,city_hotel_code=unique_hotels[hotel_count][1], hotel_name=unique_hotels[hotel_count][2])
        try:
            hotel_table.save()
        except IntegrityError as e:
            print(unique_hotels[hotel_count][2])
            print("Error while saving the hotel.")
            print(e)
    


""" function where we call functions of duplicate checking and saving for final data """
def save_to_models():
    # validate_city_hotels()
    """ now as we have clean cities and hotels, we will get the list from db also and then check for duplicates"""
    hotels, cities = validate_city_hotels()
    unique_cities = get_unique_cities(cities)
    unique_hotels = get_unique_hotels(hotels)
   
    save_cities_to_db(unique_cities)
    save_hotels_to_db(unique_hotels)
    print("fetching data and saving into database!")
    

# save_to_models()

def main():
    print("hi")
    threading.Timer(9000.0,save_to_models).start()
    save_to_models()
    print("hello")


main()