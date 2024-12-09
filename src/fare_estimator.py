import pandas as pd
import pickle
import interface
import interactivefunctions
from datetime import datetime
#Figure out date time values
def datetime_finder_outer():

    # Get the current date and time
    now = datetime.now()

    # Get the current day of the week (0=Monday, 6=Sunday)
    day_of_week = now.strftime("%A")  # Full name of the day

    # Get the current hour (24-hour format)
    current_hour = now.hour

    # Determine the current season
    month = now.month
    if month in [12, 1, 2]:
        season = "Winter"
    elif month in [3, 4, 5]:
        season = "Spring"
    elif month in [6, 7, 8]:
        season = "Summer"
    else:
        season = "Fall"

    return {
        "day_of_week": day_of_week,
        "current_hour": current_hour,
        "season": season
    }



def fare_estimation(trip_distance, passenger_count, pickup_borough, dropoff_borough):
    # Loading the pickle file
    with open('notebooks/trained_model.pkl', 'rb') as f:
        loaded_model, feature_names = pickle.load(f)  # Unpack the model and feature names

    # Create a DataFrame with the required features
    data = pd.DataFrame({
        'trip_distance_miles': [trip_distance],
        'passenger_count': [passenger_count],
        'pickup_hour': [datetime_finder_outer()['current_hour']],
        'pickup_day_of_week': [datetime_finder_outer()['day_of_week']],
        'season': [datetime_finder_outer()['season']],
        'Pickup_Borough': [pickup_borough],
        'Dropoff_Borough': [dropoff_borough]
    })

    # One-hot encode the categorical variables
    data_encoded = pd.get_dummies(data, columns=['Pickup_Borough', 'Dropoff_Borough', 'season'], drop_first=True)

    # Ensure the DataFrame has the same columns as the model was trained on
    for feature in feature_names:
        if feature not in data_encoded.columns:
            data_encoded[feature] = 0  # Add missing features with a value of 0

    # Reorder the columns to match the model's expected input
    data_encoded = data_encoded.reindex(columns=feature_names, fill_value=0)

    # Make predictions
    fare_estimate = loaded_model.predict(data_encoded)
    return fare_estimate[0]  # Return the first element of the prediction array