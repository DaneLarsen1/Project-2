#Importing libraries and dependencies
import folium
from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
import openrouteservice
import os
from dotenv import load_dotenv
from py_functions import geocode_address, check_boro

def on_submit():
    pickup_address = pickup_entry.get()
    dropoff_address = dropoff_entry.get()
    
    pickup_coords = geocode_address(pickup_address)
    dropoff_coords = geocode_address(dropoff_address)
    
    if pickup_coords and dropoff_coords:
        in_boro1, in_boro2 = check_boro(pickup_coords, dropoff_coords)
        
        if in_boro1 and in_boro2:
            result_label.config(text=f"Pickup: {pickup_coords}, Dropoff: {dropoff_coords}")
            borough_label.config(text=f"Pickup in borough: {in_boro1}, Dropoff in borough: {in_boro2}")
        else:
            result_label.config(text="One or both addresses are not in a borough.")
            borough_label.config(text="")
    else:
        result_label.config(text="Failed to retrieve coordinates.")

# Set up the Tkinter window
root = tk.Tk()
root.title("Address Geocoder")
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