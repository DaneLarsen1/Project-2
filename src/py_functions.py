import openrouteservice
import geopandas as gpd
from shapely.geometry import Point
from dotenv import load_dotenv
import os
# Load env files
load_dotenv()

# Load shapefiles
boros = gpd.read_file("data/raw/BoroughData.geojson")

#Initalizing variables
pickup_coords = None
dropoff_coords = None
def geocode_address(address):
    # Get the API key from the environment variable
    api_key = os.getenv('API_KEY')
    
    # Create a client for OpenRouteService
    client = openrouteservice.Client(key=api_key)
    
    try:
        # Geocode the address
        geocode_result = client.pelias_search(address)
        
        # Extract latitude and longitude
        coordinates = geocode_result['features'][0]['geometry']['coordinates']
        return coordinates[0], coordinates[1]  # Return (longitude, latitude)
    
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

# Example usage
# if __name__ == "__main__":
#     pickup_address = "1600 Amphitheatre Parkway, Mountain View, CA"
#     dropoff_address = "1 Infinite Loop, Cupertino, CA"
    
#     # Get coordinates for pickup and dropoff addresses
#     pickup_coords = geocode_address(pickup_address)  # Assigns the return value to pickup_coords
#     dropoff_coords = geocode_address(dropoff_address)  # Assigns the return value to dropoff_coords
    
#     # Check if coordinates were successfully retrieved
#     if pickup_coords and dropoff_coords:
#         print(f"Pickup Coordinates: {pickup_coords}")  # (longitude, latitude)
#         print(f"Dropoff Coordinates: {dropoff_coords}")  # (longitude, latitude)

#         # Check if the coordinates are within any borough
#         in_boro1, in_boro2 = check_boro(pickup_coords, dropoff_coords)
#         print(f"Pickup is in borough: {in_boro1}")
#         print(f"Dropoff is in borough: {in_boro2}")
#     else:
#         print("Failed to retrieve coordinates.")