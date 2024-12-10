Uber AI Data Preprocessing
Brief Project Description
This project focuses on preprocessing Uber trip data to clean and transform it for building an AI model that predicts the costs of Uber rides. The main objectives are to clean the data by handling missing values, removing duplicates, and validating coordinates, and to transform the data by creating new features such as pickup hour, day of the week, season, and trip distance in miles.

Table of Contents
Introduction
Data Information
Getting Started
Methodology
Results
Dependencies
Usage
Contributing
Acknowledgments
Introduction
This project aims to preprocess Uber trip data to make it suitable for building an AI model that predicts the costs of Uber rides. The preprocessing steps include cleaning the data by handling missing values, removing duplicates, and validating coordinates, as well as transforming the data by creating new features such as pickup hour, day of the week, season, and trip distance in miles. The significance of this project lies in its ability to prepare raw data for more accurate and meaningful analysis, ultimately leading to better predictions of Uber ride costs.

Data Information
Source
The data used in this project is sourced from Uber's trip records.

Description
The dataset contains information about Uber trips, including pickup and dropoff locations, times, fare amounts, and passenger counts.

Structure
The main features/variables in the dataset include:

pickup_datetime: The date and time when the trip started.
pickup_latitude: The latitude of the pickup location.
pickup_longitude: The longitude of the pickup location.
dropoff_latitude: The latitude of the dropoff location.
dropoff_longitude: The longitude of the dropoff location.
fare_amount: The fare amount for the trip.
passenger_count: The number of passengers in the trip.
Getting Started
To get started with this project, clone the repository and install the required dependencies.

Methodology
Data Loading: Load the raw Uber trip data from a CSV file.
Data Cleaning: Clean the data by handling missing values, removing duplicates, and validating coordinates.
Data Transformation: Transform the data by creating new features such as pickup hour, day of the week, season, and trip distance in miles.
Data Saving: Save the cleaned and transformed data to CSV files for further analysis.
Results
The cleaned and transformed data is saved in the processed directory as uber_data_cleaned.csv and uber_data_transformed.csv.

Dependencies
pandas
numpy
geopy
Usage
To preprocess the Uber data, run the data_preprocessing.py script.

Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

Acknowledgments
Special thanks to Uber for providing the trip data used in this project.