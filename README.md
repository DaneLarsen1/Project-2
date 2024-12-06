Features

1. Data Cleaning

Handles missing values by:

Dropping rows with missing key or fare_amount.

Filling missing passenger_count values with 0.

Converts pickup_datetime to a proper datetime format.

Ensures fare_amount is treated as a float.

Removes duplicate entries to ensure data consistency.

2. Data Transformation

Extracts new features from the data:

Pickup Hour: Extracted from the pickup_datetime column.

Day of the Week: Encodes the day (Monday=0, Sunday=6).

Season Indicator: Maps months to corresponding seasons (Winter, Spring, Summer, Fall).

Trip Distance: Calculates distance in miles between pickup and dropoff coordinates using the Haversine formula (via geopy.distance.great_circle).

3. Data Export

Cleaned and transformed data is saved to a CSV file in a data/processed directory.

Usage

Step 1: Clean the Data

Run the cleaning script to remove duplicates, handle missing values, and standardize the data.

python src/data_cleaning.py

Step 2: Transform the Data

Use the transformation script to extract new features and calculate distances.

python src/data_transformation.py

Step 3: Visualize Data (Planned)

Once the data_visualization.py module is complete, use it to generate insights and visualizations.

Dependencies

Python 3.7+

pandas

numpy

geopy