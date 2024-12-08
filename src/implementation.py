import tkinter as tk
from interface import MapApp

class MapViewer:
    def geocode_addresses(self, pickup_address, dropoff_address):
        # This function will handle geocoding the addresses
        # You can use a geocoding library like Geopy or Google Maps API here
        print(f"Geocoding Pickup Address: {pickup_address}")
        print(f"Geocoding Dropoff Address: {dropoff_address}")
        # After geocoding, you would typically get the coordinates and create a map

if __name__ == '__main__':
    root = tk.Tk()
    
    # Create an instance of MapViewer
    map_viewer = MapViewer()
    
    # Pass the map_viewer instance to the MapApp
    app = MapApp(root)
    root.map_viewer = map_viewer  # Attach the map_viewer to the root for access in the interface
    
    # Start the Tkinter event loop
    root.mainloop()