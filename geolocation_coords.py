from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import json

geolocator = Nominatim(user_agent='Getting_Geolocation.py')


# Enter a list of cities here, this can be replaced by address or even keyword (be careful, and QA the more its based on unstructured data)
cities = ['Honolulu', 'Karachi', 'Manila', 'Aberdeen', 'Shanghai', 'Munich', 'Seoul', 'Toronto', 'New York', 'Cape Town', 'Sydney', 'Paris',
          'Reykjavik', 'Kyoto', 'Rome', 'Stockholm', 'Belgrade', 'Hamburg', 'Cairo', 'Austin', 'Sao Paulo', 'Los Angeles', 'Berlin', 'Amsterdam',
          'Barcelona', 'Istanbul', 'Johannesburg']


# Function to get the latitdue and longitude for a certain city
def getdict(list):
    thinglist = []
    for city in list:
        loc = geolocator.geocode(city)
        geolat = loc.latitude
        geolong = loc.longitude
        # Creating a dictionary so it can be viewed easily
        citydict = {'type': 'Feature', 'properties': {'id': city}, 'geometry':{'type': 'Point','coordinates':[geolong,geolat,0]}}
        thinglist.append(citydict)
    return thinglist

dict_cities = getdict(cities)

master_dict = {'type' : 'FeatureCollection', 'features':[dict_cities]}
print(master_dict)

# Exporting as a Json string file if needed
with open("geoLoc.txt", 'w') as fout:
    json_dumps_str = json.dumps(master_dict, indent=4)
    print(json_dumps_str, file=fout)