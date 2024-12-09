#Libraries and dependencies
from geopy.geocoders import Nominatim
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
import requests
from dotenv import load_dotenv
import os

#Load env
load_dotenv()
#Get API key
API_KEY = os.getenv("API_KEY")
print(API_KEY)
#Loading in boros geojson
boros = gpd.read_file('data/raw/BoroughData.geojson')
                      
def geocode_address(address):
    """
    Geocode an address to get its coordinates (latitude, longitude).
    
    Parameters:
    address (str): The address to geocode.
    
    Returns:
    tuple: A tuple containing (latitude, longitude) or (None, None) if not found.
    """
    geolocator = Nominatim(user_agent="ProjectExercises")
    
    try:
        print(f"Geocoding address: {address}")  # Debugging line
        location = geolocator.geocode(address)
        
        if location is None:
            print(f"No results found for address: {address}")
            return None, None
        
        # Return (latitude, longitude)
        print(f"Coordinates found: {location.latitude}, {location.longitude}")  # Debugging line
        return location.latitude, location.longitude
    
    except Exception as e:
        print(f"Error geocoding address '{address}': {e}")
        return None, None

#Boro Checker
def check_boro(coords, boros):
    """
    Check if the given coordinates fall within any of the borough polygons.
    
    Parameters:
    coords (tuple): A tuple containing (latitude, longitude).
    boros (GeoDataFrame): A GeoDataFrame containing borough polygons.
    
    Returns:
    str: The name of the borough if found, otherwise None.
    """
    point = Point(coords[1], coords[0])  # Create a Point object (longitude, latitude)
    
    # Check if the point is within any of the borough polygons
    for _, row in boros.iterrows():
        if row['geometry'].contains(point):
            print(f"Coordinates {coords} fall within the borough: {row['boro_name']}") 
            return row['boro_name']
    
    print(f"Coordinates {coords} do not fall within any borough.")
    return None
def get_route(start_coords, end_coords):
    # Convert coordinates from (lat, long) to (long, lat)
    start_long_lat = (start_coords[1], start_coords[0])  # (longitude, latitude)
    end_long_lat = (end_coords[1], end_coords[0])  # (longitude, latitude)

    # Define the API endpoint with the API key
    url = f"https://api.openrouteservice.org/v2/directions/driving-car?api_key={API_KEY}&start={start_long_lat[0]},{start_long_lat[1]}&end={end_long_lat[0]},{end_long_lat[1]}"

    # Set up the headers for the request
    headers = {
        'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    }

    # Make the request to the OpenStreetServices API
    response = requests.get(url, headers=headers)

    # Print the response for debugging
    print(f"API Response: {response.status_code}, {response.text}")

    # Check if the request was successful
    if response.status_code == 200:
            route_data = response.json()
            print("Full API Response JSON:", route_data)  # Print the entire JSON response

            # Extracting specific information
            if 'features' in route_data and len(route_data['features']) > 0:
                distance = route_data['features'][0]['properties']['summary']['distance']
                duration = route_data['features'][0]['properties']['summary']['duration']
                line_coordinates = route_data['features'][0]['geometry']['coordinates']

                # Print distance and duration
                print(f"Total Distance: {distance} meters")
                print(f"Total Duration: {duration} seconds")
                print(f"Route Coordinates: {line_coordinates}")

                return distance, duration, line_coordinates  # Return distance, duration, and coordinates
            else:
                print("No features found in the response.")
                return None, None, None