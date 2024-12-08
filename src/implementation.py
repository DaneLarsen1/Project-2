#Importing libraries and dependencies
import folium
from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
import openrouteservice
import os
from dotenv import load_dotenv
import py_functions
from tkhtmlview import HTMLLabel

# Global variable to store the map file path
map_file = None

def on_submit():
    global map_file  # Use the global variable to store the map file path
    pickup_address = pickup_entry.get()
    dropoff_address = dropoff_entry.get()
    
    pickup_coords = py_functions.geocode_address(pickup_address)
    dropoff_coords = py_functions.geocode_address(dropoff_address)
    print(pickup_coords, dropoff_coords)
    if pickup_coords and dropoff_coords:
        in_boro1, in_boro2 = py_functions.check_boro(pickup_coords, dropoff_coords)
        
        if in_boro1 and in_boro2:
            # Get the route
            api_key = "Random"
            route = py_functions.get_route(api_key, pickup_coords, dropoff_coords)
            
            # Create the map with the route
            nyc_map = py_functions.create_map(pickup_coords, dropoff_coords, "data/raw/BoroughData.geojson", route)
            
            # Save the map to a temporary HTML file
            map_file = "nyc_route_map.html"
            nyc_map.save(map_file)
            
            # Load the HTML file into the Tkinter window
            with open(map_file, 'r') as f:
                map_html = f.read()
            
            # Create a new window to display the map
            map_window = tk.Toplevel(root)
            map_window.title("Route Map")
            html_label = HTMLLabel(map_window, html=map_html)
            html_label.pack(fill="both", expand=True)
            
            # Create a Confirm Route button
            confirm_button = tk.Button(map_window, text="Confirm Route", command=lambda: confirm_route(map_window))
            confirm_button.pack(pady=10)
        else:
            result_label.config(text="One or both addresses are not in a borough.")
            borough_label.config(text="")
    else:
        result_label.config(text="Failed to retrieve coordinates.")

def confirm_route(map_window):
    global map_file
    # Delete the HTML file
    if map_file and os.path.exists(map_file):
        os.remove(map_file)
    # Close the map window
    map_window.destroy()

# Set up the Tkinter window
root = tk.Tk()
root.title("Fare finder")

#Instructions for address format:
format_label = tk.Label(root, text="Please enter addresses in the format:\n'1600 Amphitheatre Parkway, Mountain View, CA 94043'")
format_label.pack()

tk.Label(root, text="Pickup Address:").pack()
pickup_entry = tk.Entry(root)
pickup_entry.pack()

tk.Label(root, text="Dropoff Address:").pack()
dropoff_entry = tk.Entry(root)
dropoff_entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

borough_label = tk.Label(root, text="")
borough_label.pack()

root.mainloop()