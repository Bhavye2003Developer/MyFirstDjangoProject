import folium
from folium import PolyLine

import requests

# Create a map centered at a specific location
m = folium.Map(location=[21.0000, 78.0000], zoom_start=5.5)

API_KEY_OPEN_ROUTES = "5b3ce3597851110001cf6248669180d3dc2b4b6b8b1d4408102b8ae3"
API_KEY_GEOAPIFY = "c425975697e945aaa11f5cb0512ba022"

def plot_coordinates(route_coordinates):

    route = PolyLine(locations=route_coordinates, color='red', weight=5)
    route.add_to(m)

    m.save('route_map.html')

    print(m)



def get_coordinates_route(lat_source, long_source, lat_dest, long_dest):

    if (lat_source == -1 or long_source == -1 or lat_dest == -1 or long_dest == -1):
        print("Invalid location")
        return

    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }

    # lat_source = 28.6139
    # long_source = 77.2090

    # lat_dest = 19.0760
    # long_dest = 72.8777

    url = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={API_KEY_OPEN_ROUTES}&start={long_source},{lat_source}&end={long_dest},{lat_dest}&radius=1000'

    call = requests.get(url, headers=headers)


    if (call.status_code == 200):
        print(call.status_code, call.reason)
        coordinates = call.json()['features'][0]['geometry']['coordinates']
        print(len(coordinates))
        print(url)
        for i in range(len(coordinates)):
            coordinates[i] = [coordinates[i][1], coordinates[i][0]]
        plot_coordinates(coordinates)
        

    else:
        print(call.status_code, call.reason)
        print(call.text)
        


def get_place_coordinate(place):

    #local_place country

    final_place = place.replace(" ", "%20")

    url = f"https://api.geoapify.com/v1/geocode/search?text={final_place}&format=json&apiKey={API_KEY_GEOAPIFY}"
            
    response = requests.get(url)

    if (response.status_code == 200):
        lat_long = [response.json()['results'][0]['lat'], response.json()['results'][0]['lon']]
    else:
        lat_long = [-1,-1]
        print(response.status_code, response.reason)
    return lat_long

source = input("Enter the source: ")
destination = input("Enter the destination: ")


source_coordinates = get_place_coordinate(source)
destination_coordinates = get_place_coordinate(destination)

get_coordinates_route(source_coordinates[0], source_coordinates[1], destination_coordinates[0], destination_coordinates[1])