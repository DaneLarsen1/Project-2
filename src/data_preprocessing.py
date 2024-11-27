import pandas as pd

#fill with real csv when ready
url_flu_data_1 = 'data/raw/flu_data_source_1.csv'
url_flu_data_2 = 'data/raw/flu_data_source_2.csv'

# Load datasets
flu_data_1 = pd.read_csv(url_flu_data_1)
flu_data_2 = pd.read_csv(url_flu_data_2)

# Basic exploration (optional) LEAVE FOR NOW
# print("Flu Data 1 Overview:")
# print(flu_data_1.head())
# print("Flu Data 2 Overview:")
# print(flu_data_2.head())


def clean_flu_data(data):
    # Example cleaning process
    # Assuming the dataset has these common columns; adjust as necessary
    # - 'Date': represented as date of the week
    # - 'Flu_Cases': number of reported flu cases
    
    # Converts the dates tro readable time
    if 'Date' in data.columns:
        data['Date'] = pd.to_datetime(data['Date'])
    
    # Drop duplicates
    data.drop_duplicates(inplace=True)
    
    # Drop 0s 
    if 'Flu_Cases' in data.columns:
        data['Flu_Cases'].fillna(0, inplace=True) 

    return data

flu_data_clean_1 = clean_flu_data(flu_data_1)
flu_data_clean_2 = clean_flu_data(flu_data_2)

#Combines cleaned datasets (only if we need it)
combined_flu_data = pd.concat([flu_data_clean_1, flu_data_clean_2], ignore_index=True)

# How to save to CSV files
combined_flu_data.to_csv('data/processed/flu_data_cleaned.csv', index=False)

print("Cleaned flu data saved to data/processed/flu_data_cleaned.csv.")
