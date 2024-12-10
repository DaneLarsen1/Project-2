# interface.py
import tkinter as tk
from tkinter import simpledialog, messagebox
import interactivefunctions
import folium
import webbrowser
import os
class MapApp:
    def __init__(self, master):
        self.master = master
        master.title("Map Viewer")

        self.label_pickup = tk.Label(master, text="Enter Pickup Address:")
        self.label_pickup.pack(pady=5)

        self.entry_pickup = tk.Entry(master, width=50)
        self.entry_pickup.pack(pady=5)

        self.label_dropoff = tk.Label(master, text="Enter Dropoff Address:")
        self.label_dropoff.pack(pady=5)

        self.entry_dropoff = tk.Entry(master, width=50)
        self.entry_dropoff.pack(pady=5)

        self.button = tk.Button(master, text="Get Coordinates", command=self.get_addresses)
        self.button.pack(pady=20)

    def get_addresses(self):
        pickup_address = self.entry_pickup.get()
        dropoff_address = self.entry_dropoff.get()

        if not pickup_address or not dropoff_address:
            messagebox.showwarning("Input Error", "Please enter both pickup and dropoff addresses.")
            return
        #Calling the geocoding function
        pickup_coords = interactivefunctions.geocode_address(pickup_address)
        dropoff_coords = interactivefunctions.geocode_address(dropoff_address)
        
        #Check iff coordinates are in boros
        if pickup_coords and dropoff_coords:
            pickup_boro = interactivefunctions.check_boro(pickup_coords, interactivefunctions.boros)
            dropoff_boro = interactivefunctions.check_boro(dropoff_coords, interactivefunctions.boros)

            print(f"Pickup Coordinates: {pickup_coords}, Borough: {pickup_boro}")
            print(f"Dropoff Coordinates: {dropoff_coords}, Borough: {dropoff_boro}")

            #Displaying the map with coordinate pins
            self.display_map(pickup_coords, dropoff_coords)
        
        else:
            messagebox.showwarning("Geocoding Error", "Failed to retrieve coordinates.")

    def display_map(self, pickup_coords, dropoff_coords):
        # Create a map centered around the midpoint of the pickup and dropoff coordinates
        map_center = [(pickup_coords[0] + dropoff_coords[0]) / 2, (pickup_coords[1] + dropoff_coords[1]) / 2]
        m = folium.Map(location=map_center, zoom_start=13)

        # Add markers for pickup and dropoff
        folium.Marker(location=pickup_coords, popup='Pickup Location', icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location=dropoff_coords, popup='Dropoff Location', icon=folium.Icon(color='red')).add_to(m)

        # Save the map to an HTML file
        map_file = 'map.html'
        m.save(map_file)

        # Open the map in a web browser
        webbrowser.open('file://' + os.path.realpath(map_file))

        # Create a new window for the map and the button
        self.map_window = tk.Toplevel(self.master)
        self.map_window.title("Map")

        # Add a button to find the route
        self.route_button = tk.Button(self.map_window, text="Find Route", 
                                    command=lambda: self.find_route(pickup_coords, dropoff_coords, m))
        self.route_button.pack(pady=10)

        return m

    def find_route(self, pickup_coords, dropoff_coords, m):
        # Call the get_route function with the coordinates
        distance, duration, line_coordinates = interactivefunctions.get_route(pickup_coords, dropoff_coords)

        # Print the returned values for debugging
        print("Distance:", distance)
        print("Duration:", duration)
        print("Line Coordinates:", line_coordinates)

        if line_coordinates:
            print("Route data retrieved successfully.")
            # Display the route on the map
            self.add_route_to_map(line_coordinates, m)
        else:
            print("Failed to retrieve route data.")

    def add_route_to_map(self, line_coordinates, m):
        """
        Add a route line to the existing map using the provided line coordinates.

        Parameters:
        line_coordinates (list): A list of coordinates representing the route.
        """
        # Convert coordinates to (lat, long) format
        route_line = [(coord[1], coord[0]) for coord in line_coordinates]  # Convert to (latitude, longitude)

        # Add the route line to the existing map
        folium.PolyLine(locations=route_line, color='blue', weight=5, opacity=0.7).add_to(m)

        # Optionally, you can save the updated map again
        m.save('updated_map.html')
        webbrowser.open('file://' + os.path.realpath('updated_map.html'))

if __name__ == '__main__':
    root = tk.Tk()
    app = MapApp(root)
    root.mainloop()