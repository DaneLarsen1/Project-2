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
    day_of_week_str = now.strftime("%A")  # Full name of the day

    # Mapping from day of the week to integer
    day_of_week_mapping = {
        "Monday": 0,
        "Tuesday": 1,
        "Wednesday": 2,
        "Thursday": 3,
        "Friday": 4,
        "Saturday": 5,
        "Sunday": 6
    }
    
    # Convert to integer
    day_of_week = day_of_week_mapping[day_of_week_str]

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


import pandas as pd
import pickle
from datetime import datetime

def datetime_finder_outer():
    now = datetime.now()
    day_of_week_mapping = {
        "Monday": 0, "Tuesday": 1, "Wednesday": 2,
        "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6
    }
    day_of_week = day_of_week_mapping[now.strftime("%A")]
    current_hour = now.hour
    month = now.month
    season = "Winter" if month in [12, 1, 2] else "Spring" if month in [3, 4, 5] else "Summer" if month in [6, 7, 8] else "Fall"
    
    return {"day_of_week": day_of_week, "current_hour": current_hour, "season": season}

def fare_estimation(trip_distance, passenger_count, pickup_borough, dropoff_borough):
    try:
        with open('notebooks/model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        data = pd.DataFrame({
            'trip_distance_miles': [trip_distance],
            'passenger_count': [passenger_count],
            'pickup_hour': [datetime_finder_outer()['current_hour']],
            'pickup_day_of_week': [datetime_finder_outer()['day_of_week']],
            'Pickup_Borough': [pickup_borough],
            'Dropoff_Borough': [dropoff_borough],
            'season': [datetime_finder_outer()['season']]
        })
        features = data[['trip_distance_miles', 'passenger_count', 'pickup_hour', 'pickup_day_of_week', 'season', 'Pickup_Borough', 'Dropoff_Borough']]  # Select only the required features

        features = pd.get_dummies(features, drop_first=True)

        #make prediction
        fare_estimate = loaded_model.predict(features)
        return fare_estimate[0]
    except FileNotFoundError:
        print("The trained model file was not found.")
        return None
    except Exception as e:
        print("An error occurred: ", str(e))
        return None