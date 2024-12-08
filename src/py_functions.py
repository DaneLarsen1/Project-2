import openrouteservice
import geopandas as gpd
from shapely.geometry import Point
from dotenv import load_dotenv
import os
import folium
import requests
# Load env files
load_dotenv()

# Load shapefiles
boros = gpd.read_file("data/raw/BoroughData.geojson")

#Initalizing variables
pickup_coords = None
dropoff_coords = None
def geocode_address(address):
    api_key = os.getenv('API_KEY')
    client = openrouteservice.Client(key=api_key)
    
    try:
        print(f"Geocoding address: {address}")  # Debugging line
        geocode_result = client.pelias_search(address)
        
        if not geocode_result['features']:
            print(f"No results found for address: {address}")
            return None, None
        
        # Extract coordinates and ensure they are in (latitude, longitude) order
        coordinates = geocode_result['features'][0]['geometry']['coordinates']
        print(f"Coordinates found: {coordinates}")  # Debugging line
        return coordinates[0], coordinates[1]  # Return (latitude, longitude)
    
    except Exception as e:
        print(f"Error geocoding address '{address}': {e}")
        return None, None
def check_boro(coord1, coord2):
    # Create Point objects from the coordinates
    point1 = Point(coord1)  # (longitude, latitude)
    point2 = Point(coord2)  # (longitude, latitude)

    # Check if the points are within any of the borough geometries
    in_boro1 = boros['geometry'].contains(point1).any()
    in_boro2 = boros['geometry'].contains(point2).any()

    if pickup_coords and dropoff_coords:
        print(f"Pickup Coordinates: {pickup_coords}")  # (longitude, latitude)
        print(f"Dropoff Coordinates: {dropoff_coords}")  # (longitude, latitude)

        # Check if the coordinates are within any borough
        in_boro1, in_boro2 = check_boro(pickup_coords, dropoff_coords)
        print(f"Pickup is in borough: {in_boro1}")
        print(f"Dropoff is in borough: {in_boro2}")
    else:
        print("Failed to retrieve coordinates.")

    return in_boro1, in_boro2

def create_map(pickup_coords, dropoff_coords, geojson_path, route=None):
    # Initialize the map
    nyc_map = folium.Map(location=[40.7128, -74.0060], zoom_start=12, tiles="Stamen Toner")

    # Add NYC borough outlines
    folium.GeoJson(geojson_path, name="NYC Boroughs").add_to(nyc_map)

    # Add markers for pickup and drop-off locations
    folium.Marker(pickup_coords, popup="Pickup", icon=folium.Icon(color="green")).add_to(nyc_map)
    folium.Marker(dropoff_coords, popup="Drop-off", icon=folium.Icon(color="red")).add_to(nyc_map)

    # Add route, if available
    if route:
        folium.PolyLine(route, color="blue", weight=5, opacity=0.8).add_to(nyc_map)

    # Add a layer control to toggle map elements
    folium.LayerControl().add_to(nyc_map)

    return nyc_map
def get_route(API_KEY, pickup_coords, dropoff_coords):
    # Get the API key from the environment variable
    api_key = os.getenv('API_KEY')
    
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }
    
    # Construct the URL with dynamic coordinates
    url = f'https://api.openrouteservice.org/v2/directions/driving-car?api_key={api_key}&start={pickup_coords}&end={dropoff_coords}'
    
    # Make the GET request
    response = requests.get(url, headers=headers)
    
    # Print the status code and reason
    print(response.status_code, response.reason)
    
    # Print the response text
    print(response.text)