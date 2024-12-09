#Importing libraries and dependencies
import folium
from geopy.geocoders import Nominatim
import tkinter as tk
from tkinter import Tk, Label, Entry, Button, messagebox
import openrouteservice
import os
from dotenv import load_dotenv
#Build the object and set up box
root = tk.Tk()
root.title("Route Finder and Fare Estimator")

#Get pick up address
Label(root, text="Pickup Address: ").pack()
pickup_entry = tk.Entry(root)
pickup_entry.pack()

#Get drop off address
Label(root, text="Drop off Address: ").pack()
dropoff_entry = tk.Entry(root)
dropoff_entry.pack()

#Add submit
submit_button = tk.Button(root, text="Submit", command=lambda: check_convert)