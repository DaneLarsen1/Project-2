import pandas as pd
import os

raw_data_path = 'data/raw/'
uber_data_file = 'uber.csv' 

# Combine paths
file_path = os.path.join(raw_data_path, uber_data_file)

# Step 2: Load the Uber dataset
try:
    uber_data = pd.read_csv(file_path)
except FileNotFoundError:
    print(f"File {file_path} not found. Please check the name and location.")
    raise

# Optional: Basic exploration
# print("Uber Data Overview:")
# print(uber_data.head())

def clean_uber_data(data):
    """
    Clean the Uber trip data.

    Parameters:
        data (DataFrame): The Uber trip data to clean.

    Returns:
        DataFrame: The cleaned Uber trip data.
    """

    # Step 1: Convert 'pickup_datetime' to datetime format
    if 'pickup_datetime' in data.columns:
        data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'], errors='coerce')
        
    # Step 2: Drop duplicates
    data.drop_duplicates(inplace=True)

    # Step 3: Handle missing values
    # Drop rows with missing 'key' or 'fare_amount'
    data.dropna(subset=['key', 'fare_amount'], inplace=True)

    # Fill missing 'passenger_count' with 0
    if 'passenger_count' in data.columns:
        data['passenger_count'].fillna(0, inplace=True)

    # Ensure 'fare_amount' is treated as a float
    if 'fare_amount' in data.columns:
        data['fare_amount'] = data['fare_amount'].astype(float)

    return data

# Step 4: Clean the Uber data
cleaned_uber_data = clean_uber_data(uber_data)

# Step 5: Save the cleaned Uber dataset to a CSV file
cleaned_data_path = 'data/processed/uber_data_cleaned.csv'
cleaned_uber_data.to_csv(cleaned_data_path, index=False)

print(f"Cleaned Uber data saved to {cleaned_data_path}.")